# -*- coding: utf-8 -*-
import requests
import os
import pdfplumber
from lxml import etree

import dbtools
from industry_parser.cleaning.utils import special_handling, match_industryCateName, data_pack_insert, match_cateName

url = 'http://www.csrc.gov.cn/pub/newsite/scb/ssgshyfljg/'
root_path = os.path.abspath(os.path.dirname(__file__)).split('china_industry_parser')[0]
pdf_path = str(root_path) + 'china_industry_parser\industry_parser\cleaning\images'





def get_local_industry_pdf_list():
    pdf_list = os.listdir(pdf_path)

    return pdf_list


def get_industry_pdf_title_link():
    res = requests.get(url=url)
    res.encoding = res.apparent_encoding
    html_str = res.text
    content = etree.HTML(html_str)
    title_list = content.xpath(
        "//div[@class='body_bk']/div[@class='body']/div[@class='er_main']/div[@class='er_right']/div/div[@class='fl_list']/ul//li")
    newest_pdf = title_list[0]
    title = newest_pdf.xpath("./a/text()")[0]
    link01 = newest_pdf.xpath("./a/@href")[0]
    link02 = link01.split('/')[1] + '/' + link01.split('/')[2]
    link = url + str(link02)

    return title, link


def download_industry_pdf(title, link):
    res = requests.get(url=link)
    res.encoding = res.apparent_encoding
    html_str = res.text
    content = etree.HTML(html_str)
    pdf_serial_num = content.xpath(
        "//div[@class='body_bk']/div[@class='body']/div[@class='in_main']/div[@class='content']/p/span/a/@href")[0]
    useless_text = link.split('/')[-1]
    pdf_serial_num = pdf_serial_num.split('/')[-1]
    pdf_link = link.replace(useless_text, pdf_serial_num)
    res = requests.get(url=pdf_link)
    with open(str(pdf_path) + '\\' + title + '.pdf', 'wb') as wf:
        wf.write(res.content)
        wf.close()


def parser_first(new_pdf_title_name):
    with pdfplumber.open(pdf_path + '\\' + new_pdf_title_name) as pdf:
        # 获取pdf页数page_num
        page_num = len(pdf.pages)  # 87
        all_page_text = []
        first_page = pdf.pages[0]
        texts = first_page.extract_text()
        header = texts.splitlines()[0]
        titles = texts.splitlines()[1]
        for page_num in range(page_num):
            page = pdf.pages[page_num]
            texts = page.extract_text()
            text_list = texts.splitlines()
            for text in text_list:
                if text == header or \
                        text == titles:
                    continue
                else:
                    all_page_text.append(text)
        return all_page_text


def parser_second(new_text_list):
    # 对解析错乱的数据进行调整
    # 当前的门类名称
    cur_category_name = None
    # 当前行业大类代码
    cur_industry_categories_code = None
    # 当前行业大类名称
    cur_industry_categories_name = None
    out_put_box = []
    for cur_text in new_text_list:
        cur_text_list = cur_text.split(' ')
        if len(cur_text_list) == 5:
            category_name = cur_text_list[0]
            industry_categories_code = cur_text_list[1]
            industry_categories_name = cur_text_list[2]
            security_code = cur_text_list[3]
            company_name = cur_text_list[4]
            category_name_new = special_handling(category_name)
            if category_name_new == 'A':  # 特殊情况
                # 修正行业大类名称
                cor_industry_categories_name = match_industryCateName(industry_categories_name)
                # 更新信息
                cur_industry_categories_code = industry_categories_code
                cur_industry_categories_name = cor_industry_categories_name
                # 打包并更新列表
                data_pack_insert(out_put_box, cur_category_name, cur_industry_categories_code,
                                 cur_industry_categories_name,
                                 security_code, company_name)
            else:
                # 对当前的门类名称进行对应，得到正确格式
                cor_categoryName = match_cateName(category_name)
                # 修正行业大类名称
                cor_industry_categories_name = match_industryCateName(industry_categories_name)
                # 更新当前的门类名称、行业大类代码、行业大类名称
                cur_category_name = cor_categoryName
                cur_industry_categories_code = industry_categories_code
                cur_industry_categories_name = cor_industry_categories_name
                # 打包并更新列表
                data_pack_insert(out_put_box, cur_category_name, cur_industry_categories_code,
                                 cur_industry_categories_name,
                                 security_code, company_name)
        elif len(cur_text_list) == 4:
            table_text_col1 = cur_text_list[0]
            table_text_col2 = cur_text_list[1]
            security_code = cur_text_list[2]
            company_name = cur_text_list[3]
            if table_text_col1.isdigit():
                industry_categories_code = table_text_col1
                industry_categories_name = table_text_col2
                cor_industry_categories_name = match_industryCateName(industry_categories_name)
                # 更新当前的行业大类代码、行业大类名称
                cur_industry_categories_code = industry_categories_code
                cur_industry_categories_name = cor_industry_categories_name
                data_pack_insert(out_put_box, cur_category_name, cur_industry_categories_code,
                                 cur_industry_categories_name,
                                 security_code, company_name)
            else:
                data_pack_insert(out_put_box, cur_category_name, cur_industry_categories_code,
                                 cur_industry_categories_name,
                                 security_code, company_name)
        else:
            security_code = cur_text_list[-2]
            company_name = cur_text_list[-1]
            data_pack_insert(out_put_box, cur_category_name, cur_industry_categories_code, cur_industry_categories_name,
                             security_code, company_name)

    return out_put_box


def gen_industry_box(table_box):
    industry_value_box = []
    for info in table_box:
        industry_values = """("{industry}", "{security_code}", "{company_name}")""".format(
            industry=info[0],
            security_code=info[3],
            company_name=info[4]
        )
        industry_value_box.append(industry_values)
    return industry_value_box


def to_insert_table(out_put_box):
    value_box = gen_industry_box(out_put_box)
    industry_insert_sql = """INSERT INTO industry (industry, security_code, company_name) VALUES {values}"""
    industry_insert_sql = industry_insert_sql.format(values=', '.join(value_box))
    print(industry_insert_sql)
    dbtools.query_industry(industry_insert_sql)



if __name__ == '__main__':
    # 获取文件标题与链接
    title, link = get_industry_pdf_title_link()

    # 下载文件
    download_industry_pdf(title, link)

    # 获取本地目录中文件名
    local_pdf_list = get_local_industry_pdf_list()
    new_pdf_title_name = local_pdf_list[0]

    # 解析pdf生成结构化数据
    list = parser_first(new_pdf_title_name)
    out_put_box = parser_second(list)
    to_insert_table(out_put_box)
# -*- coding: utf-8 -*-
# 门类名称
categoryName_dict = {
    '农、林、牧、渔业': 'A农、林、牧、渔业',
    '采矿业(B)': 'B采矿业',
    '制造业(C)': 'C制造业',
    '电力、热力、燃气': 'D电力、热力、燃气及水的生产和供应业',
    '建筑业(E)': 'E建筑业',
    '批发和零售业(F)': 'F批发和零售业',
    '交通运输、仓储和': 'G交通运输、仓储和邮政业',
    '住宿和餐饮业(H)': 'H住宿和餐饮业',
    '信息传输、软件': 'I信息传输、软件和信息技术服务业',
    '金融业(J)': 'J金融业',
    '房地产业(K)': 'K房地产业',
    '租赁和商务服务业': 'L租赁和商务服务业',
    '科学研究和技术服': 'M科学研究和技术服务业',
    '水利、环境和公共': 'N水利、环境和公共设施管理业',
    '居民服务、修理和': 'O居民服务、修理和其他服务业',
    '教育(P)': 'P教育',
    '卫生和社会工作业': 'Q卫生和社会工作业',
    '文化、体育和娱乐': 'R文化、体育和娱乐业',
    '综合(S)': 'S综合'
}

# 行业大类名称
industryCategoriesName_dict = {
    '皮革、毛皮、羽毛及其制':'皮革、毛皮、羽毛及其制品和制鞋业',
    '木材加工及木、竹、藤、':'木材加工及木、竹、藤、棕、草制品业',
    '文教、工美、体育和娱乐':'文教、工美、体育和娱乐用品制造业',
    '石油加工、炼焦及核燃':'石油加工、炼焦及核燃料加工业',
    '化学原料及化学制品制造':'化学原料及化学制品制造业',
    '黑色金属冶炼及压延加工':'黑色金属冶炼及压延加工业',
    '有色金属冶炼及压延加工':'有色金属冶炼及压延加工业',
    '铁路、船舶、航空航天和':'铁路、船舶、航空航天和其它运输设备制造业',
    '计算机、通信和其他电子':'计算机、通信和其他电子设备制造业',
    '电信、广播电视和卫星传':'电信、广播电视和卫星传输传输服务 ',
    '装卸搬运和其他运输代理':'装卸搬运和其他运输代理业',
    '机动车、电子产品和日用':'机动车、电子产品和日用产品修理业',
    '广播、电视、电影和影视':'广播、电视、电影和影视录音制作业'
}


not_in_pdf_sec_dict = {
        '000022':'G交通运输、仓储和邮政业/55水上运输业',
        '000511':'C制造业/30非金属矿物制品业',
        '000916':'G交通运输、仓储和邮政业/54道路运输业',
        '000979':'K房地产业/70房地产业',
        '300765':'C制造业/14食品制造业',
        '300766':'I信息传输、软件和信息技术服务业/64互联网和相关服务',
        '603681':'C制造业/26化学原料及化学制品制造业',
        '002958':'J金融业/66货币金融服务',
        '603379':'C制造业/26化学原料及化学制品制造业',
        '002952':'C制造业/39计算机、通信和其他电子设备制造业',
        '300767':'C制造业/29橡胶和塑料制品业',
        '300768':'I信息传输、软件和信息技术服务业/65软件和信息技术服务业',
        '603068':'C制造业/39计算机、通信和其他电子设备制造业',
        '300769':'C制造业/26化学原料及化学制品制造业',
        '603317':'C制造业/14食品制造业',
        '300770':'I信息传输、软件和信息技术服务业/63电信、广播电视和卫星传输传输服务',
        '300771':'C制造业/35专用设备制造业',
        '300773':'I信息传输、软件和信息技术服务业/65软件和信息技术服务业',
        '300772':'C制造业/34通用设备制造业',
        '603967':'G交通运输、仓储和邮政业/58装卸搬运和其他运输代理业',
        '603697':'C制造业/14食品制造业',
        '002953':'C制造业/38电气机械及器材制造业',
        '300778':'M科学研究和技术服务业/74专业技术服务业',
        '603267':'C制造业/39计算机、通信和其他电子设备制造业',
        '600989':'C制造业/14食品制造业',
        '300777':'C制造业/28化学纤维制造业',
        '300776':'C制造业/35专用设备制造业',
        '300775':'C制造业/37铁路、船舶、航空航天和其它设备制造业',
        '603982':'C制造业/36汽车制造业',
        '300779':'C制造业/废弃资源综合利用业',
        '603327':'C制造业/39计算机、通信和其他电子设备制造业',
        '002955':'C制造业/39计算机、通信和其他电子设备制造业',
        '300780':'C制造业/34通用设备制造业',
        '600270':'G交通运输、仓储和邮政业/58装卸搬运和其他运输代理业'
}
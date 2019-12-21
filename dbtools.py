# -*- coding: utf-8 -*-
import pymysql


db_config = {
    "industry": {
        "name": "industry",
        "ip": '127.0.0.1',
        "user": "root",
        "password": "ycf123"
    }
}


def query_industry(sql):
    common_ip = db_config['industry']['ip']
    common_user = db_config['industry']['user']
    common_password = db_config['industry']['password']
    common_dbname = db_config['industry']['name']

    db = pymysql.connect(host=common_ip, user=common_user, passwd=common_password, db=common_dbname, port=3306, charset='utf8')
    try:
        cursor = db.cursor()
        result = cursor.execute(sql)
        data = cursor.fetchall()
        db.commit()
        db.close()
        return data
    except Exception:
        print('Error Sql： ' + sql)
        db.close()

        raise Exception
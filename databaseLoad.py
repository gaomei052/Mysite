#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/2 下午3:06
# @Auther   : GaoMei
# @FileName : databaseLoad.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

import pymysql
import json

class Load(object):
    def __init__(self):
        with open('./ci.json','r') as f:
            conf = json.loads(f.read())['mysql']
            self.host = conf['mysql_host']
            self.user = conf['mysql_user']
            self.password = conf['mysql_password']
            self.port = conf['mysql_port']
            self.db = conf['mysql_database']
            self.conn = pymysql.connect(host=self.host,user=self.user,password=self.password,port=self.port,db=self.db)
            self.cursor = self.conn.cursor()

    def run(self,sql):
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        self.conn.commit()
        return self.result

    def close(self):
        self.cursor.close()
        self.conn.close()


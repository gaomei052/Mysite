#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/3/1 下午2:51
# @Auther   : GaoMei
# @FileName : getProHost.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

from modules.databaseLoad import Load

table = 'l_host'

def getHost(Project):
    sql = Load()
    pro = sql.run("select Project from %s;" % table)
    for i in pro:
        for j in i:
            if Project in j.split(','):
                project = j
    IP = sql.run("select IP,password,sshport from %s where Project='%s'" %(table,project))
    sql.close()
    for i in IP:
        return i
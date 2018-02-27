#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/27 上午10:39
# @Auther   : GaoMei
# @FileName : deploy.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com


from modules.sshapi import ssh
from modules.databaseLoad import Load

table = 'l_project'

class DeployProject:
    def __init__(self):
        #self.sql = Load()
        pass
    @property
    def ProjectName(self):
        sql = Load()
        project = sql.run('select Project from l_host;')
        sql.close()
        proList = []
        for i in project:
            if i[0]:
                for j in i:
                    for m in j.split(','):
                        proList.append('%s' %m)
            else:
                pass
        return proList

    def Appname(self,Project):
        sql = Load()
        appname = sql.run("select app from %s where project='%s'" %(table,Project))
        sql.close()
        appList = []
        for i in appname:
            if i[0]:
                for j in i:
                    for m in j.split(','):
                        appList.append('%s' %m)
            else:
                pass
        return appList
print DeployProject().Appname('token')
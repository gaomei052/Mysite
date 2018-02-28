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
    def _ProjectName(self):
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

    @property
    def _Appname(self):
        sql = Load()
        appname = sql.run("select project,app from %s;" %(table))
        sql.close()
        appdict = {}
        for i in appname:
            if i[0]:
                m,n = i
                appdict[m] = n
        return appdict

    @property
    def dict(self):
        proname = self._ProjectName
        appname = self._Appname
        prod = {}
        for i in proname:
            if i in appname.keys():
                prod[i] = appname[i]
            else:
                prod[i] = i
        return prod

    def app(self,project):
        return self.dict[project]


#print DeployProject().dict


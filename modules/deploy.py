#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/27 上午10:39
# @Auther   : GaoMei
# @FileName : deploy.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com


from modules.sshapi import ssh
from modules.databaseLoad import Load

class DeployProject:
    def __init__(self):
        self.sql = Load()
    @property
    def ProjectName(self):
        project = self.sql.run('select Project from l_host;')
        self.sql.close()
        proList = []
        for i in project:
            if i[0]:
                for j in i:
                    for m in j.split(','):
                        proList.append('%s' %m)
            else:
                proList.append('%s' %i)
        return proList


#a = DeployProject()
#print a.ProjectName
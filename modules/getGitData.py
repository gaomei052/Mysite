#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/3/1 下午3:11
# @Auther   : GaoMei
# @FileName : getGitData.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

from modules.databaseLoad import Load
from gitlab import Gitlab
import re

table = 'l_gitlab'

class Git:

    def getGit(self):
        sql = Load()
        data = sql.run("select * from %s;" % table)
        sql.close()
        for i in data:
            return i

    def getData(self,project):
        url,token,user,password = self.getGit()
        gl = Gitlab(url,token)

        for i in gl.projects.list(search=project):
            id = i.id
        pro = gl.projects.get(id)
        branch = pro.branches.list()

        tag_list = pro.tag_list
        address = pro.web_url
        branchL = []
        for i in branch:
            branchL.append(i.name)

        host = re.split(r'//',address)[1]
        add = 'http://%s:%s@%s' %(user,password,host)

        return {'url':add,'branch':branchL,'tag':tag_list}








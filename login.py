#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/2 下午2:57
# @Auther   : GaoMei
# @FileName : login.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

from modules.databaseLoad import Load

class Login(object):
    def __init__(self,username,password):
        self.user = username
        self.password = password
        self.conn = Load()

    def verificationUser(self):
        user = self.conn.run("select name from l_user where name='%s';" %self.user)
        if user:
            passA = self.conn.run("select password from l_user where name='%s'" %self.user)
            passB = self.conn.run("select password('%s');" %self.password)
            if passA == passB:
                return 1
            else:
                return 0
        else:
            return "Without the user."


    def permissionValue(self):
        per = self.conn.run("select permission from l_user where name='%s'" %self.user)
        return per[0][0]

    def close(self):
        self.conn.close()


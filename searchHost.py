#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/7 下午6:18
# @Auther   : GaoMei
# @FileName : searchHost.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

from modules.GuiApi import gui
from modules.databaseLoad import Load


def showhost():
    M = gui('Host List')
    M.Lable("IP Search",0,0)
    IP = M.Entry(1,0,ipadx=40)
    M.treeview(('IP', 200), ('Port', 70))
    sql = Load()
    hostname = sql.run("select hostname,sshport from l_host;")
    sql.close()
    for i in hostname:
        M.insert(i)
    M.loop()


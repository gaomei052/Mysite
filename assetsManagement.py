#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/3 上午11:52
# @Auther   : GaoMei
# @FileName : assetsManagement.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

from modules.GuiApi import gui
from modules.secretKeyGen import genRsa
from modules.databaseLoad import Load
import tkMessageBox
import re

def asset():
    def com():
        pubkey,privkey = genRsa()
        sql = Load()
        sql.run("insert into l_host(hostname,password,privateKey,publicKey) value (\
                '%s','%s','%s','%s')" %(IP.get(),password.get(),str(privkey),str(pubkey)))
        print IP,password
    def showhost():
        sql = Load()
        host = sql.run("select hostname from l_host;")
        hostlist = []
        for i in host:
            for j in i:
                hostlist.append(j)

        def listWork(hostlist):
            return re.sub(r'\[|\]|,','\n',str(hostlist))

        tkMessageBox.showinfo('HostList',listWork(hostlist))
    G = gui()
    G.Lable('HostName',5,0)
    IP = G.Entry(5,1)
    G.Lable('RootPassword',10,0)
    password = G.Entry(10,1)
    G.Button('Join',com,15,1)
    G.Button('ShowHosts',showhost,15,0)

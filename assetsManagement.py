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
import os

returnline = os.linesep

def asset():
    def com():
        pubkey,privkey = genRsa()
        sql = Load()
        try:
            sql.run("insert into l_host(hostname,password,privateKey,publicKey,sshport) value (\
                '%s',password('%s'),'%s','%s',%d)" %(IP.get(),password.get(),str(privkey)\
                                                  ,str(pubkey),int(Port.get())))
        except:
            a = tkMessageBox.askokcancel(title=None,message=\
                "Host is exist,(Ok) is go on,(Cancel) is return!")
            if a:
                if Port.get():
                    sql.run("update l_host set sshport=%d where hostname='%s'"
                             %(int(Port.get()),IP.get()))
                if password.get():
                    sql.run("update l_host set password='%s' where hostname='%s'"
                            % (password.get(), IP.get()))


    def showhost():
        sql = Load()
        host = sql.run("select hostname,sshport from l_host;")
        hostlist = []
        for i in host:

            hostlist.append(i)

        def listWork(hostlist):
            a = re.sub(r'\(','',str(hostlist))
            b = re.sub(r'\)',returnline,a)
            c = re.sub(r',','',b)
            d = re.sub(r'\'','\t',c)
            return re.sub(r'\[|\]',returnline,d)

        #tkMessageBox.showinfo('HostList',listWork(hostlist))
        G.message('Host',listWork(hostlist))
    G = gui("Assets Management")
    G.Lable('HostName',5,0)
    IP = G.Entry(5,1)
    G.Lable('RootPassword',10,0)
    password = G.Entry(10,1)
    G.Lable('Port',11,0)
    Port = G.Entry(11,1)
    G.Button('Join',com,15,1)
    G.Button('ShowHosts',showhost,15,0)
    G.loop()

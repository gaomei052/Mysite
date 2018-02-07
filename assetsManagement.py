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
from modules.sshapi import ssh
import tkMessageBox
import re
import os

reg = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
returnline = os.linesep

def asset():
    def com():
        if verificationIP():
            tkMessageBox.showerror('Error', 'Format example(192.168.0.55)')
            return 0
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
        sql.close()



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
        sql.close()

        #tkMessageBox.showinfo('HostList',listWork(hostlist))
        G.message('Host',listWork(hostlist))

    def test():
        A = ssh(hostname=IP.get(), Port=Port.get(), password=password.get())
        B = A.test()
        A.result()
        if IP.get() == '' and Port.get() == '' and password.get() == '':
            tkMessageBox.showerror('Error','Pleas input everyone')
            return 0
        if not verificationIP():
            tkMessageBox.showerror('Error', 'Format example(192.168.0.55)')
            return 0
        if B:
            tkMessageBox.showinfo('Seccessful','Connect tset is successful')
        else:
            tkMessageBox.showerror('Error','Connect test failed')
            return 0


    def verificationIP():
        ip = IP.get()
        if not re.match(reg,ip):
            return 0
        for i in re.split(r'\.',ip):
            if int(i) > 255:
                return 0
        return 1

    def verifip(event):
        res = verificationIP()
        if not res:
            tkMessageBox.showerror('Error', 'Format example(192.168.0.55)')

    G = gui("Assets Management")
    G.Lable('HostName',5,0)
    IP = G.Entry(5,1,key='<Tab>',fun=verifip)
    G.Lable('RootPassword',10,0)
    password = G.Entry(10,1,key='<Button-1>',fun=verifip)
    G.Lable('Port',11,0)
    Port = G.Entry(11,1,key='<Button-1>',fun=verifip)
    G.Button('Join',com,15,2)
    G.Button('ShowHosts',showhost,15,0)
    G.Button('Connect Test',test,15,1)
    G.loop()
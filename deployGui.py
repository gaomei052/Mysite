#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/2 下午5:47
# @Auther   : GaoMei
# @FileName : deployGui.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

from modules.GuiApi import gui
from modules.databaseLoad import Load
from modules.deploy import DeployProject

table = 'l_project'
table1 = 'l_gitlab'

def Deploy():
    def getApp(event):
        proname = ProName.get()
        app = DeployProject().app(proname)
        appList = []
        for i in app.split(','):
            appList.append(i)
        G.values(appList)
    appList = []

    def codeMessage():
        def OKGit():
            sql = Load()
            sql.run("insert into %s(Address,Token,user,password) values ('%s','%s','%s','%s')" \
                    %(table1,add.get(),token.get(),user.get(),password.get()))
            sql.close()
        def ShowGit():
            def gCheck(event):
                L = gui('...')
                L.Button('Delect',)

            sql = Load()
            git = sql.run("select * from %s;" %table1)
            S = gui("GIT")
            S.treeview(('Address',200),('Token',200),('User',50),('Password',100),ipady=87,Evn=gCheck)
            for i in git:
                S.insert(i)
            S.loop()


        M = gui('Gitlab Message')
        M.Lable('GitAddress',5,0)
        add = M.Entry(5,1)
        M.Lable('Token',10,0)
        token = M.Entry(10,1)
        M.Lable('User',15,0)
        user = M.Entry(15,1)
        M.Lable('Password',20,0)
        password = M.Entry(20,1)
        M.Button('OK',OKGit,25,1)
        M.Button('ShowGit',ShowGit,25,0)






        M.loop()


    def OK():
        pass



    name = DeployProject().dict.keys()
    G = gui('Deploy')
    G.Lable('Project',5,0)
    ProName = G.combobox(5,1,width=24,values=name,default=1)


    G.Lable('App',10,0)
    AppName = G.combobox(10,1,width=24,key='<Button-1>',fun=getApp,values=appList)
    G.Button('CodeMessage',codeMessage,15,0)
    G.Button('OK',OK,15,1)
    G.loop()

Deploy()
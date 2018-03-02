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
            sql.run("delect from %s" % table1)
            sql.run("insert into %s(Address,Token,user,password) values ('%s','%s','%s','%s')" \
                    %(table1,add.get(),token.get(),user.get(),password.get()))
            sql.close()
        def ShowGit():
            def gCheck(event):
                def g():
                    return S.Even()['values']
                def gOK():
                    a = add.get()
                    t = token.get()
                    u = user.get()
                    p = password.get()
                    sql = Load()
                    sql.run("delete from %s;" % table1)
                    sql.run("insert into %s(Address,Token,user,password) values ('%s','%s','%s','%s');" \
                            %(table1,a,t,u,p))
                    i = sql.run("select * from %s;" % table1)
                    sql.close()
                    S.clear()
                    for f in i:
                        S.insert(f)

                T = gui('Gitlab Message')
                T.Lable('GitAddress', 5, 0)
                add = T.Entry(5, 1,default=g()[0])
                T.Lable('Token', 10, 0)
                token = T.Entry(10, 1,default=g()[1])
                T.Lable('User', 15, 0)
                user = T.Entry(15, 1,default=g()[2])
                T.Lable('Password', 20, 0)
                password = T.Entry(20, 1,default=g()[3])
                T.Button('OK', gOK, 25, 1)
                T.loop()


            sql = Load()
            git = sql.run("select * from %s;" %table1)
            S = gui("GIT")
            S.treeview(('Address',200),('Token',200),('User',50),('Password',100),ipady=87,Eve=gCheck)
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
        Pro = ProName.get()
        App = AppName.get()
        bra = branch.get()
        t = tag.get()
        DeployProject().DepPro(Pro,App,bra,t)




    name = DeployProject().dict.keys()
    G = gui('Deploy')
    G.Lable('Project',5,0)
    ProName = G.combobox(5,1,width=24,values=name,default=1)
    G.Lable('App',10,0)
    AppName = G.combobox(10,1,width=24,key='<Button-1>',fun=getApp,values=appList)

    G.Lable('Branch',13,0)
    branch = G.Entry(13,1,ipadx=24)
    G.Lable('Tag',14,0)
    tag = G.Entry(14,1,ipadx=24)
    G.Button('CodeMessage',codeMessage,15,0)
    G.Button('OK',OK,15,1)
    G.loop()

Deploy()
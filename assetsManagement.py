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
from modules.ansible_api import command
import tkMessageBox
import re
import os

reg = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
returnline = os.linesep

table = 'l_host'
table2 = 'l_project'

def asset():
    def com():
        if not verificationIP():
            tkMessageBox.showerror('Error', 'Format example(192.168.0.55)')
            return 0
        pubkey,privkey = genRsa()
        sql = Load()
        try:
            sql.run("insert into l_host(IP,password,privateKey,publicKey,sshport,Project) value (\
                '%s','%s','%s','%s',%d,'%s')" %(IP.get(),password.get(),str(privkey)\
                                                  ,str(pubkey),int(Port.get()),\
                                                                   str(Project.get())))
        except:
            a = tkMessageBox.askokcancel(title=None,message=\
                "Host is exist,(Ok) is go on,(Cancel) is return!")
            if a:
                if Port.get():
                    sql.run("update %s set sshport=%d where IP='%s'"
                             %(table,int(Port.get()),IP.get()))
                if password.get():
                    sql.run("update %s set password='%s' where IP='%s'"
                            % (table,password.get(), IP.get()))
                if Project.get():
                    sql.run("update %s set Project='%s' where IP='%s'" \
                            %(table,Project.get(),IP.get()))
        sql.close()

    def showhost():
        def search(event):
            sql = Load()
            host = sql.run("select IP,sshport,hostname,cpu_count,cpu_core,\
                  system_kide,machine,memory,shell,kernel,pkg_message,\
                  python_version,Project from %s where IP='%s';" \
                           %(table,IP.get()))
            M = gui('Host List')
            M.treeview(('IP', 100), ('Port', 30),('HostName',100),('CPU_count',70),('CPU_core',70),('System_Kide',90),\
                   ('machine',70),('Memory',50),('shell',80),('kernel',150),('pkg_Message','90'),\
                   ('python_Version',90),('Project',150),ipady=87)
            sql = Load()
            sql.close()
            for i in host:
                M.insert(i)
            M.loop()

        def update():
            M.clear()
            sql = Load()
            host = sql.run("select IP,password,sshport from l_host;")
            for i in host:
                com = command(host=[i[0]],password=i[1],port=i[2],module='setup')
                data = com.hostMessage()
                hostname = data['hostname']
                cpu_count = data['cpu_cont']
                cpu_core = data['cpu_core']
                system_kide = data['systemKide']
                machine = data['machine']
                memory = data['memory']
                shell = data['shell']
                kernel = data['kernel']
                pkg_message = data['pkg_Message']
                python_version = data['python_version']



                sql.run('update %s set hostname="%s",cpu_count=%d,cpu_core=%d,\
system_kide="%s",machine="%s",memory=%d,shell="%s",kernel="%s",pkg_message="%s",\
python_version="%s" where IP="%s"' %(table,hostname,cpu_count,cpu_core,system_kide,\
                                 machine,memory,shell,kernel,pkg_message,\
                                 python_version,i[0]))
            hostname = sql.run("select IP,sshport,hostname,cpu_count,cpu_core,\
                  system_kide,machine,memory,shell,kernel,pkg_message,\
                  python_version,Project from l_host;")

            for i in hostname:
                M.insert(i)
            sql.close()

        def cod(event):
            sql = Load()
            a = M.Even()['values'][-1]
            S = gui('Project')
            S.treeview(('Project',100),('App',200),ipady=87)
            for i in a.split(','):
                appname = sql.run("select * from %s where project='%s'"\
                                  %(table2,i))
                for j in appname:
                    S.insert(j)
            sql.close()
            S.loop()

        M = gui('Host List')
        M.Lable("IP Search", 0, 0)
        IP = M.Entry(1, 0, ipadx=40,key='<Return>',fun=search)
        M.Button('Update',update,2,0,width=30)
        M.treeview(('IP', 100), ('Port', 30),('HostName',100),('CPU_count',70),('CPU_core',70),('System_Kide',90),\
                   ('machine',70),('Memory',50),('shell',80),('kernel',150),('pkg_Message','90'),\
                   ('python_Version',90),('Project',150),ipady=87,Eve=cod)
        sql = Load()
        hostname = sql.run("select IP,sshport,hostname,cpu_count,cpu_core,\
                  system_kide,machine,memory,shell,kernel,pkg_message,\
                  python_version,Project from l_host;")
        sql.close()

        for i in hostname:

            M.insert(i)
        M.loop()

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

    def JoinApp():
        def OK():
            sql = Load()
            try:
                sql.run("insert into %s(project,app) values ('%s','%s')" \
                        %(table2,projectname.get(),appname.get()) )
            except:
                a = tkMessageBox.askokcancel(title=None, message= \
                    "Host is exist,(Ok) is go on,(Cancel) is return!")
                if a:
                    sql.run("update %s set app='%s' where project=%s" \
                            %(table2,appname.get(),projectname.get()))

            sql.close()
        def show():
            sql = Load()
            pro = sql.run("select * from %s;" % table2)
            sql.close()
            T = gui("Show App")
            T.treeview(('Project',100),('App',200),ipady=87)
            for i in pro:
                T.insert(i)
            T.loop()
        proj = Project.get()
        a = proj.split(',')
        M = gui('Append App')
        M.Lable('Project',10,0)
        projectname = M.combobox(10,1,values=a)
        M.Lable('App',15,0)
        appname = M.Entry(15,1)
        M.Button('OK',OK,20,1,columnspan=2)
        M.Button('Show',show,20,0)
        M.loop()

    G = gui("Assets Management")
    G.Lable('HostName',5,0)
    IP = G.Entry(5,1,key='<Tab>',fun=verifip)
    G.Lable('RootPassword',10,0)
    password = G.Entry(10,1,key='<Button-1>',fun=verifip)
    G.Lable('Port',11,0)
    Port = G.Entry(11,1,key='<Button-1>',fun=verifip)
    G.Lable('Project',12,0)
    Project = G.Entry(12,1)
    G.Button('...',JoinApp,12,2)
    G.Button('Join',com,15,2)
    G.Button('ShowHosts',showhost,15,0)
    G.Button('Connect Test',test,15,1)
    G.loop()

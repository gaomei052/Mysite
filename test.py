#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/2 下午3:24
# @Auther   : GaoMei
# @FileName : test.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com


from modules import databaseLoad

a = databaseLoad.Load()
#a.run("insert into l_user(name,password,permission) value ('gaomei',password('gaomei'),0),('test1',password('gaomei'),1),('test2',password('gaomei'),2),('test3',password('gaomei'),3);")
#a.run("create table l_user(id int not null primary key auto_increment,name char(20) not null unique key,password varchar(255) not null,permission int);")
#print a.run("select permission from l_user where name='gaomei'")[0][0]
#a.run("create table l_host(id int not null primary key auto_increment,\
#                            IP varchar(255) not null unique key,\
#                            password varchar(255) not null,\
#                            privateKey text,\
#                            publicKey text,\
#                            sshport int not null,\
#                            hostname varchar(255),\
#                            cpu_count int,\
#                            cpu_core int,\
#                            system_kide VARCHAR(255),\
#                            machine CHAR(40),\
#                            memory int,\
#                            shell VARCHAR(255),\
#                            kernel VARCHAR(255),\
#                            pkg_message char(40),\
#                            python_version char(10);")

#print a.run("select hostname from l_host;")
#b =  a.run('select IP from l_host where IP="192.168.0.33";')
#print b
#for i in b:
#    print i[0]
#a.run("create table l_project(project char(40) not null unique key,\
#app varchar(255))")
a.run("create table l_gitlab(Address VARCHAR(255) not null,\
Token VARCHAR(255) not null,user char(40) not null,password char(40) not null);")
#print a.run("select project,app from l_project;")
a.close()

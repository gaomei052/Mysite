#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/2 下午5:47
# @Auther   : GaoMei
# @FileName : deployGui.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

from modules.GuiApi import gui
from modules.deploy import DeployProject

def Deploy():
    name = DeployProject().ProjectName
    G = gui('Deploy')
    G.Lable('Project',5,0)
    ProName = G.combobox(5,1,width=24,values=name)
   # ProName = G.Entry(5,1,columnspan=2)
    G.Lable('App',10,0)
    AppName = G.Entry(10,1,columnspan=2)
    G.loop()
#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/2 下午5:47
# @Auther   : GaoMei
# @FileName : deployGui.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

from tkinter import *
from tkinter import ttk
from tkFileDialog import *
import tkMessageBox
from login import Load

def Deploy():
    top = Tk()
    top.title("DeployGUI")
    Label(top,text='Project').grid(row=5,column=0)
    ProjectName = StringVar()
    Project = Entry(top,textvariable=ProjectName)
    Project.grid(row=5,column=1,columnspan=2)
    Label(top,text='App').grid(row=10,column=0)
    AppName = StringVar()
    App = Entry(top,textvariable=AppName)
    App.grid(row=10,column=1,columnspan=2)
    top.mainloop()

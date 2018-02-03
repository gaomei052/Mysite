#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/3 上午11:54
# @Auther   : GaoMei
# @FileName : GuiApi.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

from tkinter import *
from tkinter import ttk
from tkFileDialog import *
import tkMessageBox

class gui(object):
    def __init__(self):
        self.top = Tk()

    def Button(self,name,command,row,column,width=None,height=None,columnspan=None):
        B = Button(self.top,text=name,command=command)
        if height and width:
            B = Button(self.top, text=name, command=command,width=width,height=height)
        if width:
            B = Button(self.top, text=name, command=command,width=width)
        if height:
            B = Button(self.top, text=name, command=command,height=height)

        if columnspan:
            B.grid(row=row,column=column,columnspan=columnspan)
        else:
            B.grid(row=row, column=column)
        return B

    def Lable(self,name,row,column,columnspan):
        L = Label(self.top,text=name)
        L.grid(row=row,column=column,columnspan=columnspan)
        return L

    def Entry(self,row,column,columnspan,show,default):
        V = StringVar()
        E = Entry(self.top,textvariable=V)
        E.grid(row=row,column=column,columnspan=columnspan)
        if show:
            E['show'] = show
        if default:
            V.set(default)
        result = V.get()
        return result


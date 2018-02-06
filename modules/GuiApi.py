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
    def __init__(self, name):
        self.top = Tk()
        self.top.title(name)
        self.screen_width = self.top.winfo_screenwidth()
        self.screen_height = self.top.winfo_screenheight() - 200

    def Button(self, name, command, row, column, width=None, height=None, columnspan=None):
        B = Button(self.top, text=name, command=command)
        if height and width:
            B = Button(self.top, text=name, command=command, width=width, height=height)
        if width:
            B = Button(self.top, text=name, command=command, width=width)
        if height:
            B = Button(self.top, text=name, command=command, height=height)

        if columnspan:
            B.grid(row=row, column=column, columnspan=columnspan)
        else:
            B.grid(row=row, column=column)
        return B

    def Lable(self, name, row, column, columnspan=None):
        L = Label(self.top, text=name)
        if columnspan:
            L.grid(row=row, column=column)
        else:
            L.grid(row=row, column=column, columnspan=columnspan)
        return L

    def Entry(self, row, column, show=None, default=None, columnspan=None,key=None,fun=None):
        self.V = StringVar(self.top)
        E = Entry(self.top, textvariable=self.V)
        if columnspan:
            E.grid(row=row, column=column)
        else:
            E.grid(row=row, column=column, columnspan=columnspan)
        if show:
            E['show'] = show
        if default:
            self.V.set(default)
        if key and not fun:
            pass
        if fun and not key:
            pass
        if key and fun:
            E.bind(key,fun)
        return self.V

    def message(self,title,msg):
        top = Tk()
        top.title(title)

        Message(top,text=msg).grid()
        self.loop(master=top)


    def loop(self,master=None):
        if master:
            self.top = master
        self.top.update_idletasks()
        self.top.deiconify()
        self.top.withdraw()
        w = self.top.winfo_width()+ 10
        h = self.top.winfo_height() + 10
        self.top.geometry('%sx%s+%s+%s' % (w,h,(self.screen_width-w)/2,\
                                           (self.screen_height-h)/2))
        self.top.deiconify()
        Frame(self.top,height=5).grid()
        self.top.mainloop()

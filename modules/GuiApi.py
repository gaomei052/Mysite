#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/3 上午11:54
# @Auther   : GaoMei
# @FileName : GuiApi.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tkFileDialog import *
import tkMessageBox


class gui(object):
    def __init__(self, name=None):
        self.top = Tk()
        if name:
            self.top.title(name)
        self.screen_width = self.top.winfo_screenwidth()
        self.screen_height = self.top.winfo_screenheight() - 200
        self.frame = Frame(self.top)



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

    def Lable(self, name, row, column, columnspan=None, ipadx=None):
        L = Label(self.top, text=name)
        if columnspan:
            L.grid(row=row, column=column)
        else:
            L.grid(row=row, column=column, columnspan=columnspan)
        if ipadx:
            L.grid(row=row, column=column, ipadx=ipadx)
        return L

    def Entry(self, row, column, show=None, default=None, columnspan=None, key=None, fun=None, ipadx=None):
        self.V = StringVar(self.top)
        E = Entry(self.top, textvariable=self.V)
        if columnspan:
            E.grid(row=row, column=column)
        else:
            E.grid(row=row, column=column, columnspan=columnspan)
        if ipadx:
            E.grid(row=row, column=column, ipadx=ipadx)
        if show:
            E['show'] = show
        if default:
            self.V.set(default)
        if key and not fun:
            pass
        if fun and not key:
            pass
        if key and fun:
            E.bind(key, fun)
        return self.V

    def combobox(self,row,column,width=None,values=None,key=None,fun=None,default=None):
        width = width or 20
        values = values or ''
        data = StringVar(self.top)
        self.com = ttk.Combobox(self.top,width=width,textvariable=data)
        self.com.grid(row=row,column=column)
        if key and fun:
            self.com.bind(key,fun)
        self.com['values'] = values
        self.com.current(default)

        return data

    def values(self,values):
        self.com['values'] = values



    def message(self, title, msg):
        top = Tk()
        top.title(title)

        Message(top, text=msg).grid()
        self.loop(master=top)


    def treeview(self,*args, **kwargs):
        self.frame.grid()
        scrollBar = Scrollbar(self.frame)
        if 'ipady' in kwargs.keys():
            h = kwargs['ipady']
        else:
            h = 1
        scrollBar.grid(row=10,column=1,ipady=h)

        mid = []
        for i in range(len(args)):
            mid.append('c' + str(i))
        midtuple = tuple(mid)
        self.treeview = Treeview(
            self.frame,
            columns=midtuple,
            show='headings',
            yscrollcommand=scrollBar.set
        )
        e = iter(args)
        f = iter(midtuple)

        def a():
            try:
                self.treeview.column(f.next(), width=e.next()[1], anchor='center')
                return a()
            except:
                return

        a()
        n = iter(args)
        m = iter(midtuple)

        def s():
            try:
                self.treeview.heading(m.next(), text=n.next()[0])
                return s()
            except:
                return

        s()
        self.treeview.grid(row=10,column=0, sticky=W, rowspan=10)
        scrollBar.config(command=self.treeview.yview)

        if 'Eve' in kwargs.keys():
            self.treeview.bind('<Double-Button-1>',kwargs['Eve'])


    def Even(self):
        a = self.treeview.focus()
        return self.treeview.item(a)

    def insert(self, *args):
        for i in args:
            self.treeview.insert('', 0, values=i)

    def clear(self):
        items = self.treeview.get_children()
        [self.treeview.delete(item) for item in items]


    def loop(self, master=None):
        if master:
            self.top = master
        self.top.update_idletasks()
        self.top.deiconify()
        self.top.withdraw()
        w = self.top.winfo_width()
        h = self.top.winfo_height()
        self.top.geometry('%sx%s+%s+%s' % (w, h, (self.screen_width - w) / 2, \
                                           (self.screen_height - h) / 2))

        self.top.deiconify()
        # Frame(self.top,height=5).grid()
        self.top.mainloop()

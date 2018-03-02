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
        self._top = Tk()
        if name:
            self._top.title(name)
        self._screen_width = self._top.winfo_screenwidth()
        self._screen_height = self._top.winfo_screenheight() - 200
        self._frame = Frame(self._top)



    def Button(self, name, command, row, column, width=None, height=None, columnspan=None):
        B = Button(self._top, text=name, command=command)
        if height and width:
            B = Button(self._top, text=name, command=command, width=width, height=height)
        if width:
            B = Button(self._top, text=name, command=command, width=width)
        if height:
            B = Button(self._top, text=name, command=command, height=height)

        if columnspan:
            B.grid(row=row, column=column, columnspan=columnspan)
        else:
            B.grid(row=row, column=column)
        return B

    def Lable(self, name, row, column, columnspan=None, ipadx=None):
        L = Label(self._top, text=name)
        if columnspan:
            L.grid(row=row, column=column)
        else:
            L.grid(row=row, column=column, columnspan=columnspan)
        if ipadx:
            L.grid(row=row, column=column, ipadx=ipadx)
        return L

    def Entry(self, row, column, show=None, default=None, columnspan=None, key=None, fun=None, ipadx=None):
        self._V = StringVar(self._top)
        E = Entry(self._top, textvariable=self._V)
        if columnspan:
            E.grid(row=row, column=column)
        else:
            E.grid(row=row, column=column, columnspan=columnspan)
        if ipadx:
            E.grid(row=row, column=column, ipadx=ipadx)
        if show:
            E['show'] = show
        if default:
            self._V.set(default)
        if key and not fun:
            pass
        if fun and not key:
            pass
        if key and fun:
            E.bind(key, fun)
        return self._V

    def combobox(self,row,column,width=None,values=None,key=None,fun=None,default=None):
        width = width or 20
        values = values or ''
        data = StringVar(self._top)
        self._com = ttk.Combobox(self._top,width=width,textvariable=data)
        self._com.grid(row=row,column=column)
        if key and fun:
            self._com.bind(key,fun)
        self._com['values'] = values
        self._com.current(default)

        return data



    def values(self,values):
        self._com['values'] = values



    def message(self, title, msg):
        top = Tk()
        top.title(title)

        Message(top, text=msg).grid()
        self.loop(master=top)


    def treeview(self,*args, **kwargs):
        self._frame.grid()
        scrollBar = Scrollbar(self._frame)
        if 'ipady' in kwargs.keys():
            h = kwargs['ipady']
        else:
            h = 1
        scrollBar.grid(row=10,column=1,ipady=h)

        mid = []
        for i in range(len(args)):
            mid.append('c' + str(i))
        midtuple = tuple(mid)
        self._treeview = Treeview(
            self._frame,
            columns=midtuple,
            show='headings',
            yscrollcommand=scrollBar.set
        )
        e = iter(args)
        f = iter(midtuple)

        def a():
            try:
                self._treeview.column(f.next(), width=e.next()[1], anchor='center')
                return a()
            except:
                return

        a()
        n = iter(args)
        m = iter(midtuple)

        def s():
            try:
                self._treeview.heading(m.next(), text=n.next()[0])
                return s()
            except:
                return

        s()
        self._treeview.grid(row=10,column=0, sticky=W, rowspan=10)
        scrollBar.config(command=self._treeview.yview)

        if 'Eve' in kwargs.keys():
            self._treeview.bind('<Double-Button-1>',kwargs['Eve'])


    def Even(self):
        a = self._treeview.focus()
        return self._treeview.item(a)

    def insert(self, *args):
        for i in args:
            self._treeview.insert('', 0, values=i)

    def clear(self):
        items = self._treeview.get_children()
        [self._treeview.delete(item) for item in items]


    def loop(self, master=None):
        if master:
            self._top = master
        self._top.update_idletasks()
        self._top.deiconify()
        self._top.withdraw()
        w = self._top.winfo_width()
        h = self._top.winfo_height()
        self._top.geometry('%sx%s+%s+%s' % (w, h, (self._screen_width - w) / 2, \
                                           (self._screen_height - h) / 2))

        self._top.deiconify()
        # Frame(self._top,height=5).grid()
        self._top.mainloop()

#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/8 下午2:16
# @Auther   : GaoMei
# @FileName : test1.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

from tkinter import *
import sys


def getstr(enven):
    list = []
    for i in T.get('0.0','end').split('\n'):
        list.append(i)
    print list[-2],T.index('0.0'),T.tag_names()
    T.insert('%s.0' %(len(list)),'\ntom',END)


top  = Tk()
top.title('test')
hei = top.winfo_screenheight()
wid = top.winfo_screenwidth()
sorl = Scrollbar(top)
sorl.pack(side=RIGHT,fill=Y)
T = Text(top,height=33,background='white')
T['yscrollcommand'] = sorl.set
T.pack()
T.bind('<Return>',getstr)
sorl['command'] = T.yview()
top.update_idletasks()
top.deiconify()
top.withdraw()
w = top.winfo_height()
h = top.winfo_width() - 64
top.geometry("%dx%d+%d+%d" %(w,h,(wid-w)/2,(hei-h)/2))
top.deiconify()
top.mainloop()








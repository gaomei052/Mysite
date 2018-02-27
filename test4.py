#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/14 下午5:52
# @Auther   : GaoMei
# @FileName : test4.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

import tkinter as tk

def getstr():
    if text.get() != '':
        words = text.get()
        label["text"] = words


root = tk.Tk()
root.title('主窗口')
root.geometry('500x500')
root.wm_attributes('-topmost', 1)

text = tk.Entry(root, borderwidth=1, width=40)
text.grid(row=1, column=1)
label = tk.Label(root, text="您好")
label.grid(row=2, column=1)
comand = tk.Button(root, text="获取", command=getstr, width=10, height=2)
comand.grid(row=3, column=1)
root.mainloop()

#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/7 下午2:52
# @Auther   : GaoMei
# @FileName : test2.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

from GuiApi import gui
from databaseLoad import Load


def text():
    G = gui()
    G.treeview(('name',88),('age',44),ipady=88)
    G.loop()
text()
#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/3/1 下午2:39
# @Auther   : GaoMei
# @FileName : judgeModule.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

import json

def judge(file):
    with open(file,'r') as f:
        dict = json.load(f)
        if 'bastionHost' in dict:
            return 1
        else:
            return 0
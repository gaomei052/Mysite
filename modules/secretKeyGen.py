#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/5 下午1:55
# @Auther   : GaoMei
# @FileName : secretKeyGen.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

import rsa
import re

def genRsa():
    (pubkey, privkey) = rsa.newkeys(1024)
    pubkey = re.split(r'\(|,|\)',str(pubkey))[1]
    privkey = re.split(r'\(|,|\)',str(privkey))[1]
    return (int(pubkey),int(privkey))


#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/5 下午4:26
# @Auther   : GaoMei
# @FileName : sshapi.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

import paramiko

class ssh():
    def __init__(self,hostname,Port=22,password=None,privKey=None):
        self.host = hostname
        self.port = Port
        self.password = password
        self.privkey = privKey
        self.tran = paramiko.Transport((self.host,self.port))
        if self.password:
            self.tran.connect(username='root',password=self.password)
        elif self.privkey:
            priv = paramiko.RSAKey.from_private_key(self.privkey)
            self.tran.connect(username='root',pkey=priv)



    def __call__(self, *args, **kwargs):
        if self.password or self.privkey:
            return 1
        else:
            return 0

    def run(self,command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.tran
        i,o,e = ssh.exec_command(command)
        ssh.close()
        return (o.read(),e.read())

    def tranFile(self,method,src,dest):
        sftp = paramiko.SFTPClient.from_transport(self.tran)
        try:
            if method == 'put':
                sftp.put(src,dest)
            if method == 'get':
                sftp.get(src,dest)
        except Exception as e:
            return e

    def result(self):
        self.tran.close()






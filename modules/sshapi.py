#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/5 下午4:26
# @Auther   : GaoMei
# @FileName : sshapi.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

import paramiko

class ssh():
    def __init__(self,hostname=None,Port=22,password=None,privKey=None):
        try:
            self.host = hostname
            self.port = Port
            self.password = password
            self.privkey = privKey
            if self.port:
                self.port = 22
            self.tran = paramiko.Transport((self.host,self.port))
            if self.password:
                self.tran.connect(username='root',password=self.password)
            elif self.privkey:
                priv = paramiko.RSAKey.from_private_key(self.privkey)
                self.tran.connect(username='root',pkey=priv)
            self.sftp = paramiko.SFTPClient.from_transport(self.tran)
            self.ssh = paramiko.SSHClient()
        except:
            pass



    def __call__(self, *args, **kwargs):
        if self.password or self.privkey:
            return 1
        else:
            return 0

    def run(self,command):
        try:
            self.ssh._transport = self.tran
            i,o,e = self.ssh.exec_command(command)
            return (o.read(),e.read())
        except:
            return 0

    def tranFile(self,method,src,dest):
        try:
            if method == 'put':
                self.sftp.put(src,dest)
            if method == 'get':
                self.sftp.get(src,dest)
        except Exception as e:
            return e

    def test(self):
        try:
            if self.run(''):
                return 1
            else:
                return 0
        except:
            return 0

    def result(self):
        try:
            self.ssh.close()
            self.sftp.close()
            self.tran.close()
        except:
            return 0

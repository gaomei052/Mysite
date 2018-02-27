#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/9 上午10:03
# @Auther   : GaoMei
# @FileName : ansible_api.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com


from ansible.runner import Runner
from ansible.inventory import Inventory
from ansible.playbook import PlayBook
import json


class command(object):
    def __init__(self,
                 host=None,
                 user='root',
                 password=None,
                 port=None,
                 module=None,
                 args=None,
                 privRsa=None,
                 ):
        self.host = host or '127.0.0.1'
        self.password = password or ''
        self.user = user or 'root'
        self.port = port or 22
        self.module = module or 'ping'
        self.args = args or ''
        self.privRsa = privRsa or ''

    @property
    def In(self):
        return Inventory(self.host)

    def run(self):
        pm = Runner(
            remote_pass=self.password,
            private_key_file=self.privRsa,
            remote_port=self.port,
            remote_user=self.user,
            inventory=self.In,
            timeout=5,
            forks=10,
            module_name=self.module,
            module_args=self.args,
            subset='all',
        )
        out = pm.run()
        return out

    def resultJson(self):
        return json.dumps(self.run(),indent=1,sort_keys=True,separators=(',',':'))

    def hostMessage(self):
        IP = self.host[0]
        setup = self.run()['contacted'][IP]['ansible_facts']
        hostname = setup['ansible_hostname']
        systemKide = setup['ansible_distribution']+setup['ansible_distribution_version']
        runCont = setup['ansible_product_name']
        machine = setup["ansible_machine"]
        shell = setup['ansible_user_shell']
        kernel = setup['ansible_kernel']
        pkg_Message = setup['ansible_pkg_mgr']
        cpu_core = setup['ansible_processor_cores']
        cpu_cont = setup['ansible_processor_count']
        python_version = setup['ansible_python_version']
        memory = setup['ansible_memtotal_mb']

        desc = {'IP':IP,'hostname':hostname,'systemKide':systemKide,\
                'runCont':runCont,'machine':machine,'shell':shell,'kernel':kernel,\
                'pkg_Message':pkg_Message,'cpu_core':cpu_core,
                'cpu_cont':cpu_cont,'python_version':python_version,'memory':memory}

        return desc

#a = command(host=['123.103.123.90'],password='slot747 tagS',module='setup')
#print a.hostMessage()
#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/8 下午5:19
# @Auther   : GaoMei
# @FileName : test2.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

import ansible.runner
import ansible.playbook
import ansible.inventory
from ansible import callbacks
from ansible import utils
import json

# the fastest way to set up the inventory

# hosts list
hosts = ["192.168.0.55","192.168.0.56"]
# set up the inventory, if no group is defined then 'all' group is used by default
example_inventory = ansible.inventory.Inventory(hosts)

pm = ansible.runner.Runner(
    remote_user='root',
    remote_pass='test',
    module_name='setup',
    private_key_file='',
    timeout=5,
    inventory=example_inventory,
    subset='all'  # name of the hosts group
)
print ansible.inventory.In
out = pm.run()
di =  out['contacted']['192.168.0.55']['ansible_facts']
print json.dumps(di,sort_keys=True,indent=4)


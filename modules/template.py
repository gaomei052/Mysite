#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import re

class Template(object):
    '''
    example:
        A = Template(templatefile,descconfigfile)
        A.sub(port=3306,address='192.168.0.1',path='/path/to/path')
    '''
    def __init__(self,templatefile,config):
        self.templatefile = templatefile
        self.config = config
        self.reg = re.compile(r'{{(\b\w+\b)}}')

    def sub(self,**kwargs):
        with open(self.templatefile,'r+') as filename1, open(self.config,'w') as filename2:
            for line in filename1.readlines():
                if re.findall(r'{{\b\w+\b}}',line):
                    pass
                else:
                    filename2.write(line)
                for i in kwargs.keys():
                    if re.findall(r'{{%s}}' % i,line):
                        filename2.write(re.sub(r'{{%s}}' % i,kwargs[i],line))
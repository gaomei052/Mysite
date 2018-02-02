#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from tornado.httpclient import HTTPClient

def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body


print synchronous_fetch('http://www.baidu.com')
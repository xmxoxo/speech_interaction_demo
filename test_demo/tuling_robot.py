#!/usr/bin/env python3
#coding:utf-8

__author__ = 'xmxoxo<xmxoxo@qq.com>'

import requests
import json


def answer(message, key):
    url = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=' + message
    res = requests.get(url)
    res.encoding = 'utf-8'
    answer_message = json.loads(res.text)
    return answer_message

if __name__ == '__main__':
    pass


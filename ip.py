#!/usr/bin/env python
#coding:utf-8
import requests

url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url+''
                         '')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")
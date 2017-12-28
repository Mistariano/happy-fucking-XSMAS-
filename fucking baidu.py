# coding:utf-8
__author__ = 'Mistariano'

import requests
import re

url="http://www.baidu.com/s?wd=bzoj"

r = requests.get(url)
body=r.content.decode('utf-8')
# print(body)

res=re.findall('href=\"(http://www\.baidu\.com/link\?url=.*?)\"',body)
# print(res)
for u in res:
    print(u)
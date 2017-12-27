# coding:utf-8
__author__ = 'Mistariano'

import re
import requests
import json

res=[]
for i in range(1,50):
    print("%d:"%(i))
    url = "http://www.lydsy.com/JudgeOnline/problemset.php?page="+str(i)
    r=requests.get(url=url)
    body=r.content.decode('utf-8')
    pattern='<a href=\'problem\.php\?id=[0-9]*?\'>(.*?)<'
    result=re.findall(pattern,body)
    for r in result:
        res.append(r)

json_str=json.dumps(res)
print json_str
json_data=json.loads(open('out.out','r').read())
# print json_data
for a in json_data:
    print(a)
open('out.out','w').write(json_str)
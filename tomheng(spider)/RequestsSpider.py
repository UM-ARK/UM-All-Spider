from email.header import Header
from tkinter.tix import Tree
from urllib import response
import requests
from lxml import html
import json

userName = "141414@umac.mo"
passWord = "123456"
authMethod = ['FormsAuthentication','other']

data = {
    "UserName":userName,
    "Password":passWord,
    "AuthMethod": 'FormsAuthentication'
}

url = 'https://isw.um.edu.mo/siapp/faces/home'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

# 請求 cookies
# cookieJar = respon.cookies
# cookie = cookieJar.get_dict()

s = requests.session()
s.post(url=url,headers=header,data=data)
respon = s.get(url=url,headers=header)
print(respon.status_code)

with open("result.html","w",encoding='utf-8') as f:
    f.write(respon.content.decode())

#ujb6wg4LWFvW0HVRQqEKLtlpKAWHNVqEX0CxGUqZ9W1XKEwR-es2!-1523218477!180521783
#https://websso.um.edu.mo/adfs/ls/?wa=wsignin1.0&wtrealm=urn:federation:prod:cas&wctx=eba19313-365e-4087-ba28-2f5a80d29788&client-request-id=f1f8daef-0340-4e0d-d800-0080015000a9

#https://websso.um.edu.mo/adfs/ls/?wa=wsignin1.0&wtrealm=urn:federation:prod:cas&wctx=eba19313-365e-4087-ba28-2f5a80d29788&client-request-id=f1f8daef-0340-4e0d-d800-0080015000a9
import requests
"""
get
"""
url1 = 'https://www.kuaidi100.com/query'
payload = {'type':'shunfeng','postid':'SF1409812547112'}
res1 = requests.get(url=url1,params=payload)
print(res1.text)

"""
post
"""
url = 'https://wanandroid.com/user/login'
data = {"username": "liangchao","password": "123456"}
res = requests.post(url= url,data=data)
# 查看响应状态码
print(res.status_code)
# 查看响应信息
print(res.text)
# 查看响应头
print(res.headers)
# 查看请求头
print(res.request.headers)
# 查看cookie
print(res.cookies)
# 查看请求url
print(res,url)
# 响应信息转字典
print(res.json())

import json
data = {"username": "liangchao","password": "123456"}
json2 = '{"username": "liangchao", "password": "123456"}'
# 字典转json
json1 = json.dumps(data)
print(json1)
# json转字典
dict1 = json.loads(json2)
print(dict1)

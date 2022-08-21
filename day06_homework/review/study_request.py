import requests
# cookie
url = 'https://wanandroid.com/user/login'
data = {"username": "ymw001", "password": "123456"}
res = requests.post(url=url,data=data)
cookie = res.cookies
print(res.headers)
print(res.text)

# 接口依赖登录接口的cookie信息
url2 = "https://wanandroid.com//user/lg/userinfo/json"
# res1 = requests.get(url=url2,cookies=cookie)
# print(res1)

# header
header = {}
header['cookie']='JSESSIONID=67CBE7164A77C7A79FB9E3CBA611B136'
res2 = requests.get(url=url2,headers=header)
print(res2.text)

# session
import requests.sessions
url = 'https://wanandroid.com/user/login'
data = {"username": "ymw001", "password": "123456"}
# 登录后session会记录cookie信息，后续可以使用
s = requests.session()
res = s.post(url=url,data=data)

url2 = "https://wanandroid.com//user/lg/userinfo/json"
res1 = s.get(url=url2)
print(res.text)
print(res1.text)
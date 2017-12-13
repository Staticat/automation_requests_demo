import json
import requests
from requests import exceptions

URL = 'https://api.github.com'

def bulid_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def custom_request():
    from requests import Request,Session
    s = Session()       #初始化一个Seesion
    headers = {'User-Agent':'fake1.3.4'}# fake是伪装的意思，就是设置一个假的
    request = Request('GET',bulid_uri('user/emails'),auth=('171129658@qq.com','282418Asd'),headers=headers)
    prepped = request.prepare() #初始化一个prepare对象，用来包装请求headers和body
    print(prepped.body)
    print(prepped.headers)

    respones = s.send(prepped,timeout=5) # 通过session对象调用发送请求，内容是prepped包装好的请求
    print(respones.status_code)
    print(respones.headers)
    print(respones.text)

if __name__ == '__main__':
    custom_request()

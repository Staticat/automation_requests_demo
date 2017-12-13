import requests
import json

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])  #主要作用是拼接请求借口请求地址

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4) #采用json里面提供方法打印出来，格式更好看


def request_method():
    response = requests.get(build_uri('users/Staticat'))  #调用get方法，注意用户名这个地方写法，没有图片中冒号
    print(better_output(response.text)) #调用json更好格式输出

if __name__=='__main__':
    request_method()
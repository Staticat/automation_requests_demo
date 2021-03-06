import json
import requests

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    response = requests.get(build_uri('users/Staticat'))
    print(better_output(response.text))

def params_method():
    response = requests.get(build_uri('users'),params={'since':11})
    print(better_output(response.text))
    print(response.headers)
    print(response.url)

def json_method():
    response = requests.get(build_uri('user'),auth=('171129658@qq.com','282418Asd'),
                            json={'email':'171129658@qq.com','name':'Jpanda'})
    print(better_output(response.text))
    print(response.headers)
    print(response.url)

if __name__=='__main__':
    json_method()
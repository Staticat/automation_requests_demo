import json
import requests

URL='https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    response = requests.delete(build_uri('user/emails'),auth=('171129658@qq.com','282418Asd'),
                               json=['13713886382@163.com'])
    # print(better_output(response.text))
    print(response.request.headers)
    print(response.request.body)

if __name__=='__main__':
    request_method()
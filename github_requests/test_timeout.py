import json
import requests
from requests import exceptions

URL = 'https://api.github.com'

def bulid_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def timeout_request():

    try:
        respones = requests.get(bulid_uri('user/emails'),auth=('171129658@qq.com','282418Asd'),
                                timeout=10)
    except exceptions.Timeout as e:
        print(str(e))
    else:
        print(respones.text)

if __name__=='__main__':
    timeout_request()

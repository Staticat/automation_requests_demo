import requests

Base_Url = 'https://api.github.com'

def bulid_uri(end_ponit):
    return '/'.join([Base_Url,end_ponit])

def basic_auth():

    response = requests.get(bulid_uri('user'),auth=('171129658@qq.com','282418Asd'))
    print(response.status_code)
    print(response.text)
    print(response.request.headers)

if __name__=='__main__':
    basic_auth()
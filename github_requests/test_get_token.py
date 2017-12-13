import requests

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def oauth_auth():

    headers = {'Authorization':'token 3ca6e2105b82ed7bc3dd9c1e16f2712217b1af63'}
    respnose = requests.get(build_uri('user'),headers=headers)
    print(respnose.status_code)
    print(respnose.text)
    print(respnose.request.headers)


oauth_auth()
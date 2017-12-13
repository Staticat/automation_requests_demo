import requests
from contextlib import closing

def download_image():

    url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1512102492728&di=9cd16d61144589c22b5229c1b53cb4af&imgtype=0&src=http%3A%2F%2Fpic.baike.soso.com%2Fp%2F20140415%2Fbki-20140415104220-671149140.jpg'
    response = requests.get(url,stream=True)
    with closing(requests.get(url,stream=True)) as response:
        with open('selenium3.jpg','wb') as file:
            for data in response.iter_content(10):
                file.write(data)
    # response = requests.get(url)
    print(response.status_code)
    # print(response.content)

if __name__=='__main__':
    download_image()
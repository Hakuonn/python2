import requests

data1={'username':'黃天受','password':'0000'}
response=requests.get('http://140.127.149.184/testget.php',params=data1)
if response.status_code==200:
    print(response.content.decode('utf-8'))



data2={'lang':'tw','type':'2'}
response=requests.get('https://apis.youbike.com.tw/api/front/station/all',params=data2)
if response.status_code==200:
    print(response.content.decode('utf-8'))


for i in range(5):
    response=requests.get('https://www.google.co.jp/landing/motto/tabplay/{i}.jpg'.format(i))
    if response.status_code==200:
        f=open('{i}.jpg'.format(i),'wb')
        f.write(response.content)
        f.close()

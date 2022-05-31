import requests
import json

response = requests.get('https://www.costco.com.tw/store-finder/search?q=%E8%87%BA%E7%81%A3&page=0')
if response.status_code == 200:
    aa = response.content.decode('utf-8')
    # json -> str
    tmp = json.loads(aa)
    # str --> json
    f = open('costco.json' , 'wb')
    aa1 = json.dumps(tmp,indent=4, ensure_ascii=False).encode('utf-8')
    f.write(aa1)
    f.close()


    # 網路上擷取資料 loads dumps
    # 電腦裡擷取資料 load  dump
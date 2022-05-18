import json
f = open('D:\python\程設2\youbike_station.json', 'r', encoding='utf-8')
data = json.load(f)
f.close()
ubike = data['retVal']

totalKey = [key for key,value in ubike[0].items()]

totalValue = []
for i in ubike:
    tmpValue = [value for key,value in i.items()]
    totalValue.append(tmpValue)

# json -> csv
tmpHeader = ','.join(totalKey)
tmpValue = ''
for i in totalValue:
    tmp = ','.join([str(k) for k in i]) + '\n'
    tmpValue += tmp


csvUbike = open('Ubike.csv' , 'w' , encoding='utf-8')
csvUbike.write(tmpHeader)
csvUbike.write(tmpValue)
csvUbike.close()

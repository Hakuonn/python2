import json
#load：string -> jsonObject
#dump：jsonObject -> str


f = open('costco.json', 'r', encoding='utf-8')
data = json.load(f) # str -> json Object
f.close()
display = data['data']

totalValue = []
for i in display:
    totalKey = []
    tmpValue = []
    for key, value in display[0].items():
        totalKey.append(key)
        tmpValue.append(value)
    totalValue.append(tmpValue)

print(totalKey)
print(len(totalValue))


# list generator
totalKey2 = [key for key, value in display[0].items()]
print(totalKey2)

# totalValue2 = []
# for i in display:
#     tmpValue = [value for key, value in i.items()]
#     totalValue2.append(tmpValue)

totalValue2 = [[value for key,value in i.items()] for i in display]
print(len(totalValue2))

# json -> csv
tmpHeader = ','.join(totalKey)
print(tmpHeader)
tmpValue = ''
for i in totalValue2:
    tmp = ','.join([str(k) for k in i]) + '\n'
    tmpValue = tmpValue + tmp
print(tmpValue)

kk = open('costco.csv', 'w', encoding='utf-8')
kk.write(tmpHeader)
kk.write(tmpValue)
kk.close()

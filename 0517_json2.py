import json
f = open('D:\python\程設2\youbike_station.json', 'r', encoding='utf-8')
data = json.load(f)
f.close()
ubike = data['retVal']

totalKey = [key for key,value in ubike[0].items()]

# totalValue = []
# for i in ubike:
#     tmpValue = [value for key,value in i.items()]
#     totalValue.append(tmpValue)
# 以下為更簡潔
totalValue = [[value for key,value in i.items()]for i in ubike]

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

# csotco
f = open('D:\python\程設2\costco.json', 'r' , encoding='utf-8')
data = json.load(f)
f.close()
co = data['data']
totalKey = [key for key,value in co[0].items()]

totalValue = [[value for key,value in i.items()]for i in co]

Header = ','.join(totalKey)
value = ''
for i in totalValue:
    tmp = ','.join(str(j) for j in i) + '\n'
    value += tmp
print(value)

testcsv = open('costco.csv' , 'w' ,encoding='utf-8')
testcsv.write(Header)
testcsv.write(value)
testcsv.close()
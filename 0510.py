'''
class Person:
    def __init__(self , name , age ,hight , weight):
        self.name = name
        self.age = age
        self.hight = hight
        self.weight = weight

group = []

f = open('0510.csv','r',encoding='utf-8')
result = f.readlines()
for i in result:
    tmp = i.split(',')
    name = tmp[0]
    age = tmp[1]
    hight = tmp[2]
    weight = tmp[3].split('\n')[0]
    # print(name + ' ' +  age + ' ' + hight + ' ' + weight)
    kk = Person(name , int(age) , int(hight) , int(weight))
    group.append(kk)
f.close()
'''

'''
class Transaction:
        def __init__(self , a , b , c , d , e):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e

covid = open("D:\python\wordspace\covid19_tw.csv","r",encoding='utf-8')
result = covid.readlines()
# header = result[0] 表頭元素
result.pop(0) #剔除title
recode = []
for i in result:
    tmp=i.split('\n')[0].split(',')
    print(tmp)
    通報日 = tmp[0]
    法定傳染病通報 = float(tmp[1])
    居家檢疫送驗 = float(tmp[2])
    擴大監測送驗 = float(tmp[3])
    Total = float(tmp[4])
    kkbox = Transaction(通報日,法定傳染病通報,居家檢疫送驗,擴大監測送驗,Total) 
    recode.append(kkbox)
covid.close()
'''

class header:
    def __init__(self,Riverside_Park,Location,Latitude,Longitude,Type):
        self.Riverside_Park = Riverside_Park
        self.Location = Location
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.Type =  Type
        

riverside = open("D:/python/wordspace/riverside_ok.csv",'r',encoding='utf-8')
result = riverside.readlines()
result.pop(0)
for i in result:
    tmp = i.split('\n')[0].split(',')
    Riverside_Park = tmp[0]
    Location = tmp[1]
    Latitude = tmp[2]
    Longitude = tmp[3]
    Type = tmp[4]
    aaa = header(Riverside_Park,Location,Latitude,Longitude,Type)
    print(aaa.Riverside_Park , ' ' , aaa.Location , ' ' , aaa.Latitude , ' ' , aaa.Longitude , ' ' , aaa.Type)
riverside.close()
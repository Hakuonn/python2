#延續上禮拜，做圖表在colab

#py 連接 mysql
import pymysql
import json

conn = pymysql.connect(host='140.127.149.184' , port=3306 , user='ic' ,passwd='ic' ,db='ic' , charset='utf8') #建立連線
#cursor = conn.cursor() #建立游標(下命令)的通道
cursor = conn.cursor(pymysql.cursors.DictCursor) #建立游標通道並將傳回結果轉成dict
# cursor.execute("CREATE TABLE `ic`.`C110156217` ( `name` VARCHAR(10) NOT NULL) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;") #新增資料表
cursor.execute("INSERT INTO `ic`.`C110156217` (`name` , `id`) VALUES ('handsome' , 'c110156187');") #新增一筆紀錄
# cursor.execute("DROP TABLE C110156217;") #刪除資料表
#查詢資料表
cursor.execute("SELECT * FROM `C110156217`;") #選擇資料表
rows = cursor.fetchall() #擷取資料回來
for i in rows:
    print(i) #裡面的type是turple ,如果cursor有先設定dict則type為dict

data=[]
for i in rows:
    data.append(i)
print(data)
# json Object -> byte str
tmp = json.dumps(data ,indent=4 , ensure_ascii=False)
print(tmp)

conn.commit()
cursor.close()
conn.close()


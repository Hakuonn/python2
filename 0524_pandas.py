import imp
import pandas as pd
import json



# Series -> 一維資料 (list+dict 整合 -> Series)
data = pd.Series([80,90,50,30] , index=['國文','英文','數學','社會'])
print(data)
print(data.index)
print(data.values)
print(data['國文'])
print(data['英文' : '社會'])
print(data[['英文' , '社會']])
print(data[ : :-1])


data1 = pd.Series([100,50,70,35])
print(data1)
print(data1[0])
print(data1[0 : 2])
print(data1[[0,3]])
print(data1[ : :-1])


data2 = pd.Series({'國文' : 80 , '英文' : 40 ,'數學' :85 ,'社會' : 100})
print(data2)


# dataframe -> 多個一維陣列所組合而成
grade_python = pd.Series({'c101' : 40 , 'c102' : 20 ,'c103' :95 ,'c104' : 80})
print(grade_python)
grade_php = pd.Series({'c101' : 100 , 'c102' : 50 ,'c103' :90 ,'c104' : 60})
print(grade_php)
grade_calculus = pd.Series({'c101' : 70 , 'c102' : 80 ,'c103' : 10 ,'c104' : 40})
print(grade_php)
grade_total =pd.DataFrame({'python2' : grade_python , '網頁程式設計' : grade_php , 'calculus' : grade_calculus})
print(grade_total)

grade_linux = pd.Series({'c101' : 70 , 'c102' : 80 ,'c103' : 10 ,'c105' : 40})
print(grade_php)
states =pd.DataFrame({'python2' : grade_python , '網頁程式設計' : grade_php , 'calculus' : grade_calculus ,'linux' : grade_linux})
print(states)

print(grade_total.index)
print(grade_total.values)
print(grade_total.columns)
print(grade_total.shape)



f = open('D:\python\程設2\costco.json', 'r' , encoding='utf-8')
#str -> dict
data = json.load(f)
f.close()

tmp = data['data']
print(tmp)
print(type(tmp))

df = pd.DataFrame(tmp)
print(df)
print(df.shape)
print(df.columns)
print(df.values)

df.to_csv('costco_pandas.csv' , index=False , header=False , encoding='utf-8') 
# header 對應 columns
df.to_excel('costco_pandas.xlsx' , index=False)
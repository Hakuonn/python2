from numpy import NaN
import pandas as pd
import json

# dataframe -> 多個一維陣列所組合而成
grade_python = pd.Series({'c101': 40, 'c102': 20, 'c103': 95, 'c104': 80})
grade_php = pd.Series({'c101': 100, 'c102': 50, 'c103': 90, 'c104': 60})
grade_calculus = pd.Series({'c101': 70, 'c102': 80, 'c103': 10, 'c104': 40})
grade_total = pd.DataFrame(
    {'python2': grade_python, 'php': grade_php, 'calculus': grade_calculus})

print(grade_total)
print(grade_total.index)
print(grade_total.columns)
print(grade_total.values)
print(grade_total.shape)  # 幾欄幾列
print(grade_total.head(2))  # 看頭兩筆資料
print(grade_total.tail(2))  # 看最後兩筆資料
print(grade_total.describe())  # 敘述型資料
print(grade_total.T)  # transpose轉置
print(grade_total.T.describe())


# slice 切片
# col切片
print(grade_total['python2'])
print(grade_total[['python2', 'php']])

# row切片
print(grade_total.loc['c102'])
print(grade_total.loc[['c102', 'c101']])
print(grade_total.iloc[1])
print(grade_total.iloc[[1, 3]])

# selection by index , column label
print(grade_total.loc[['c102', 'c101'], ['calculus', 'php']])
# selection by postion
print(grade_total.iloc[[1, 3], [1, 2]])

print(grade_total.iloc[:, [1, 2]])  # ：-> all

print(grade_total.iloc[::-1, :: -1])

print(grade_total)
grade_total.iloc[[1, 3], [1, 2]] = NaN
print(grade_total)
tmp = grade_total.drop('calculus', axis=1)  # 刪除直行 -> axis = 1
tmp = grade_total.drop('c103', axis=0)  # 刪除橫列 -> axis = 0
print(tmp)

tmp1 = grade_total.dropna(axis=0)  # 把橫列NaN的資料清除掉
print(tmp1)


tmp2 = grade_total.fillna(value=59)  # 填value給NaN欄位
print(tmp2)

print(grade_total['python2'] >= 60)
print(grade_total[grade_total['python2'] >= 60])  # 直接把python2當作條件判斷式





# 範例
f = open('youbike_station.json', 'r', encoding='utf-8')
data = json.load(f)
f.close()
tmp = data['retVal']
df = pd.DataFrame(tmp)
print(df)

# 減法方式
df2 = df.drop(['address_cn', 'address_en', 'img'], axis=1)
print(df2)
print(df2['area_code'].value_counts())
df3 = df2[df2['area_code'] == '08']
print(df3.shape)

# 加法方式
df2 = df[['area_code', 'district_tw', 'parking_spaces', 'name_tw']]
print(df2)
print(df2.shape)

print(df2.loc[0, 'area_code'])  # selection by label
print(df2.iloc[0, 0])  # selection by postion

print(df2['area_code'].value_counts())

tptmp = df2[df2['area_code'] == '00']
print(tptmp)
print(tptmp.groupby('district_tw').count())  # groupby -> 值相同把它算再一起

result = tptmp.groupby('district_tw').count()['name_tw']
print(result.sort_values())

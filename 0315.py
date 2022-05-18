tmp = [0,1,2,3]
tmp2=[9,8,7,6]
tmp.append(4)#新增一個元素
tmp.pop() #刪除一個元素(指定位置,若無則刪除最後一個)
tmp.insert(2,5)#插入一個數(位置,數字)
print(len(tmp))
abc=tmp.copy()#複製list
abc.append(6)
abc.clear()#將list清空
tmp.sort()#將list從小到大排列
tmp.reverse()#反轉list
tmp2.extend(tmp)#追加另一個序列中的多個值

#氣泡排序法
grades=[60,70,35,55,90]
for i in range(len(grades)-1):
    for j in range(len(grades)- i - 1 ):
        if grades[j]>grades[j+1]:
            grades[j],grades[j+1]=grades[j+1],grades[j]
print(grades)

#list1
grades1=[12,23,34,45]
sum=0
for i in range(len(grades1)):
    sum+=grades1[i]
print(sum)

#list2
grades2=[60,70,35,55,90]
max=0
min=100
for i in range(len(grades2)):
    if grades2[i]>max:
        max=grades2[i]
    elif grades2[i]<min:
        min=grades2[i]
print(max)
print(min)

#list3
grades3=[[96,65,73],[88,76,82],[92,84,89],[82,73,64],[70,83,68]]
for i in range(len(grades3)):
    sum=0
    av=0
    for j in range(3):
        print(grades3[i][j],end=" ")
        sum+=grades3[i][j]
    av=sum/3
    print(av)

for i in range(len(grades3[0])):
    sum=0
    av=0
    for j in range(len(grades3)):
        print(grades3[j][i],end=" ")
        sum+=grades3[j][i]
        av=sum/6
    print(av)
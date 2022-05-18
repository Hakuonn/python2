from posixpath import split


print("Hello World")

grade=45
grade=grade+10
print(grade)

if grade>=60:
    print("pass")
if grade<60:
    print("fail")

year=1997
month=3
day=28

sum=(year//1000)+(year%1000//100)+(year%100//10)+(year%10)+(month//10)+(month%10)+(day//10)+(day%10)

while True:
    if  sum>=10:
        sum=sum//10+sum%10
    else:
        print(sum)
        break

print(type(grade))




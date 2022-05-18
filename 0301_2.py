from random import randrange


birthday = '19971231'
sum = 0
for i in birthday:
    sum = sum+int(i)
print(sum)

if sum >= 10:
    sum = sum//10+sum % 10

if sum >= 10:
    sum = sum//10+sum % 10
print(sum)


print(list(range(1, 11, 2)))

sum = 0
for i in list(range(1, 11)):
    sum = sum+i
print(sum)

sum = 0
for i in range(11):
    sum += i
print(sum)

sum = 0
a = 0
b = 0
for i in range(1, 11, 2):
    a += i
for j in range(10, 0, -2):
    b += j
sum = a-b
print(sum)

sum = 0
for i in list(range(1, 11)):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
print(sum)


sum = 0
for i in list(range(1, 11, 2)):
    sum = sum+i-(i+1)
print(sum)

sum = 0
for i in list(range(1, 11)):
    if i % 4 == 1 or i % 4 == 0:
        sum = sum+i
    else:
        sum = sum-i
print(sum)

a = 0
for i in list(range(1, 11)):
    if i % 2 == 0:
        a -= 1/i
    else:
        a += 1/i
print(a)

b = 1
for i in (range(2, 11)):
    if i % 2 == 0:
        b -= (i-1)/i
    else:
        b += (i-1)/i
print(b)

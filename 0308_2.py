from pickle import TRUE
from platform import java_ver


sum = 65
for i in range(0, 6):
    sum += i
    print(chr(sum), end="")

# 靠左星星
for i in range(5):
    for j in range(i+1):
        print("*", end='')
    print()

# 靠右星星
for i in range(5):
    for j in range(5, i, -1):
        print(" ", end='')
    for j in range(i+1):
        print("*", end='')
    print()

# 置中星星(一)
for i in range(5):
    for j in range(5, i, -1):
        print(" ", end='')
    for j in range(i+1):
        print("*", end='')
    for j in range(1, i+1):
        print("*", end='')
    print()

# 置中星星(二)
for i in range(5):
    for j in range(4-i):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()


# 偶數空格 星星
for i in range(6):
    for j in range(5-i):
        print(" ", end="")
    for j in range(2*i+1):
        if j % 2 == 0:
            print(" ", end='')
        else:
            print("*", end="")
    print()

# 偶數空格 菱形
for i in range(2):
    if i == 0:
        for i in range(6):
            for j in range(6-i):
                print(" ", end="")
            for j in range(2*i+1):
                if j % 2 == 0:
                    print(" ", end="")
                else:
                    print("*", end="")
            print()
    else:
        for i in range(4, 0, -1):
            for j in range(6-i):
                print(" ", end="")
            for j in range(2*i+1, 1, -1):
                if j % 2 == 0:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

#butterfly
for i in range(2):
    if i == 0 :
        for i in range(5):
            for j in range(i+1):
                print("*",end="")
            for j in range(8-2*i):
                print(" ",end="")
            for j in range(i+1):
                print("*",end="")
            print()
    else:
            for i in range(4,0,-1):
                for j in range(i):
                    print("*",end="")
                for j in range(10-2*i):
                    print(" ",end="")
                for j in range(i):
                    print("*",end="")
                print()



######################以下練習###################################
# 靠左星星(遞增)
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()

# 靠左星星(遞減)
for i in range(5):
    for j in range(4,i,-1):
        print("*",end="")
    print()

# 靠右星星(遞增)
for i in range(5):
    for j in range(4,i,-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()

# 靠右星星(遞減)
for i in range(6):
    for j in range(i):
        print(" ",end="")
    for j in range(5,i,-1):
        print("*",end="")
    print()

# 置中星星
for i in range(5):
    for j in range(5,i,-1):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()

# 置中星星 偶數空格
for i in range(5):
    for j in range(5,i,-1):
        print(" ",end="")
    for j in range((i*2)+1):
        if j%2==0:
            print(" ",end="")
        else:
            print("*",end="")
    print()

# 偶數空格 菱形
for i in range(2):
    if i == 0 :
        for i in range(5):
            for j in range(4,i,-1):
                print(" ",end="")
            for j in range(2*i+1):
                if j%2==0:
                    print(" ",end="")
                else:
                    print("*",end="")
            print()
    else:
        for i in range(4,0,-1):
            for j in range(5-i):
                print(" ",end="")
            for j in range(2*i-1):
                if j%2==0:
                    print(" ",end="")
                else:
                    print("*",end="")
            print()

#butterfly
for i in range(2):
    if i == 0 :
        for i in range(5):
            for j in range(i+1):
                print("*",end="")
            for j in range(8-2*i):
                print(" ",end="")
            for j in range(i+1):
                print("*",end="")
            print()
    else:
            for i in range(4,0,-1):
                for j in range(i):
                    print("*",end="")
                for j in range(10-2*i):
                    print(" ",end="")
                for j in range(i):
                    print("*",end="")
                print()
import random
tmp = [1, 2, 3, 4, 5]
tmp1 = tuple(tmp)
tmp[0] = 99

grade = []
for i in range(1, 56):
    grade.append(random.randint(0, 100))


tmpk = "c1101562"
id = []
for i in range(1, 56):
    id.append(tmpk+'{0:02d}'.format(i))


tmp2 = {"c110156201": {'國文': 33, '英文': 99, '數學': 6}, "c110156202": {
    '國文': 66, '英文': 77, '數學': 87}, "c110156203": 100}  # dict{key:value}

print(grade[0])
print(tmp2["c110156201"])

tmp2['c110156201']['國文'] = 2
tmp2['c110156204'] = 77
tmp2['c110156205'] = 87

tmp3 = {}
for i in range(1, 56):
    tmp3[id[i]] = grade[i]

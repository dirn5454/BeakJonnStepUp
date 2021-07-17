num=[]
for i in range(3):
    num.append(int(input()))
result = str(num[0]*num[1]*num[2])
for i in range(10):
    print(result.count(str(i)))


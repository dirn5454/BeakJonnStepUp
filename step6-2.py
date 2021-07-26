a=[]
def d(n):
    sum = n
    for i in str(n):
        sum += int(i)
    return(sum)
for i in range(1,10001):
    a.append(d(i))
for i in range(1,10001):
    if i not in a:
        print(i)
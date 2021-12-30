n = int(input())
n = 1000-n
coin = [500,100,50,10,5,1]
count = 0
for i in coin:
    if i > n:
        continue
    else:
        count += n//i
        n -= (n//i)*i
print(count)
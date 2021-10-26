n,k = map(int, input().split())
clist=[]
count = 0
for i in range(n):
    coin = int(input())
    if coin <= k:
        clist.append(coin)
clist.reverse()
for i in clist:
    if k >= i:
        count += k//i
        k = k%i
print(count)
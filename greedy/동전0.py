n, k = map(int, input().split())
clist = []
count = 0
for i in range(n):
    coin = int(input())
    clist.append(coin)
clist.sort()
clist.reverse()
for i in clist:
    if i > k:
        continue
    else:
        count += k//i
        k -= (k//i)*i
print(count)
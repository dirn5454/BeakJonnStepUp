n = int(input())
nlist = list(map(int, input().split()))
nlist.sort()
sum=0
for i in range(n):
    if sum + 1 >= nlist[i]:
        sum += nlist[i]
    else:
        print(sum+1)
        break
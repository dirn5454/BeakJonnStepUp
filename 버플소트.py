n = int(input())
nlist = list(map(int, input().split()))
count = 0
temp = 0
for i in range(n-1):
    for j in range(n-1):
        if nlist[j] > nlist[j+1]:
            temp = nlist[j+1]
            nlist[j+1] = nlist[j]
            nlist[j] = temp
            count += 1
print(count)
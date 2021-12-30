n = int(input())
nlist = list(map(int, input().split()))
nlist = sorted(nlist)
count = 0
for i in range(len(nlist)):
    count += sum(nlist)
    nlist.pop()
print(count)
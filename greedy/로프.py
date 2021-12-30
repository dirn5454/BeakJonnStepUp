n = int(input())
nlist = []
clist = []
for i in range(n):
    nlist.append(int(input()))
nlist.sort()
i = 0
while len(nlist) != 0:
    clist.append(len(nlist)*nlist[0])
    nlist.pop(0)
print(max(clist))
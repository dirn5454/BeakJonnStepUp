n = int(input())
nlist = []
clist = []
j = 0
count = 1
for i in range(n):
    nlist.append(int(input()))
while nlist != clist:
    if clist[-1] <= nlist[j]:
        clist.append(count)
        print('+')
    else:
        j += 1

    count += 1
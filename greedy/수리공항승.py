n,len_ = map(int, input().split())
nlist = list(map(int, input().split()))
nlist.sort()
count = 1
start_n = nlist[0]
for i in range(len(nlist)-1):
    if nlist[i+1] - start_n < len_:
        continue
    else:
        count+=1
        start_n = nlist[i+1]
print(count)
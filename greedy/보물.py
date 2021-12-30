n = int(input())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
count = 0
alist.sort()
for i in alist:
    count += i*max(blist)
    blist.pop(blist.index(max(blist)))    
print(count)
import sys
n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
clist = []
count = 0
max_num = 0
for i in nlist:
    if i > max_num:
        max_num = i
        count = 0
    else:
        count += 1
    clist.append(count)
print(max(clist))
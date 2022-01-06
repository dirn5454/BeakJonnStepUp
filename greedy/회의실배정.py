import sys
n = int(sys.stdin.readline())
nlist = []
for i in range(n):
    nlist.append(list(map(int, sys.stdin.readline().split())))
nlist = sorted(nlist, key= lambda x : (x[1], x[0]))
number = nlist[0][1]
result_list = []
result_list.append(number)
for i in range(1, n):
    if number <= nlist[i][0]:
        result_list.append(nlist[i][1])
        number = nlist[i][1]
print(len(result_list))
import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    abs_list = []
    nlist = list(map(int, sys.stdin.readline().split()))
    nlist.sort()
    for j in range(2,n):
        abs_list.append(abs(nlist[j]-nlist[j-2]))
    print(max(abs_list))
    #다시 풀어볼 것
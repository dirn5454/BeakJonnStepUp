import sys
n = int(sys.stdin.readline())
nlist=[]
for i in range(n):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        nlist.append(order[1])
    elif order[0] == 'top':
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist[-1])
    elif order[0] == 'size':
        print(len(nlist))
    elif order[0] == 'empty':
        if len(nlist) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'pop':
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist.pop(0))
    elif order[0] == 'back':
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist[-1])
    elif order[0] == 'front':
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist[0])
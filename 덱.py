import sys
from collections import deque
n = int(sys.stdin.readline())
nlist = deque()

for i in range(n):
    order = list(sys.stdin.readline().split())

    if order[0] == 'push_front':
        nlist.appendleft(order[1])
    elif order[0] == 'push_back':
        nlist.append(order[1])
    elif order[0] == 'pop_front':
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist.popleft())
    elif order[0] == 'pop_back':
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist.pop())
    elif order[0] == 'size':
        print(len(nlist))
    elif order[0] == 'empty':
        if len(nlist) == 0:
            print(1)
        else:
            print(0)
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
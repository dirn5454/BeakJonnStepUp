n = int(input())
clist = []
if str(n)[-1] != '0':
    print(-1)
else:
    clist.append(n//300)
    n -= (n//300)*300
    clist.append(n//60)
    n -= (n//60)*60
    clist.append(n//10)
    n -= (n//10)*10

    for i in range(len(clist)):
        print(clist[i], end=' ')
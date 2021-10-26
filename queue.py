n = int(input())
queue=[]
for i in range(n):
    test = input().split()
    if test[0] == 'push':
        queue.append(test[1])
    elif test[0] =='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
            queue.remove(queue[0])
    elif test[0] == 'size':
        print(len(queue))
    elif test[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif test[0] =='front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])       
    elif test[0] =='back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])    



    
n = int(input())
stack=[]
for i in range(n):
    test = input().split()
    if test[0] =='push':
        stack.append(test[1])
    elif test[0] =='top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif test[0] =='size':
        print(len(stack))
    elif test[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif test[0] =='pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
n = int(input())
arr =[]
for i in range(n):
    arr = input()
    sum = 0
    c = 1
    for i in arr:
        if i == 'O':
            sum += c
            c += 1
        else:
            c=1
    print(sum)




def hansu(n):
    hansu = 0
    for i in range(1, n+1):
        if i < 100:
            hansu += 1
        else:
            num = list(map(int, str(i)))
            if num[0]-num[1] == num[1]-num[2]:
                hansu += 1
    return hansu
n = int(input())
print(hansu(n))


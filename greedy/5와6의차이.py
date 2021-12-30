a, b = input().split()
for i in range(len(a)):
    maxa = a.replace('5','6')
for i in range(len(b)):
    maxb = b.replace('5','6')
for i in range(len(a)):
    mina = a.replace('6','5')
for i in range(len(b)):
    minb = b.replace('6','5')
print(int(mina)+int(minb), int(maxa)+int(maxb))
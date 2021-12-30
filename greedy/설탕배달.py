n = int(input())
count = 0
while n != 0:
    if n % 5 == 0:
        count += n//5
        n -= (n//5)*5
    elif n > 2:
        n -= 3
        count += 1
    elif n == 2 or n == 1:
        count = -1
        n = 0
print(count)
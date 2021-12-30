import sys
c = list(sys.stdin.readline().strip())
c2 = []
n = int(sys.stdin.readline())
for i in range(n):
    a = list(sys.stdin.readline().split())
    if a[0] == 'L':
        if c:
            c2.append(c.pop())
        else:
            continue
    elif a[0] == 'D':
        if c2:
            c.append(c2.pop())
        else:
            continue
    elif a[0] == 'B':
        if c:
            c.pop()
        else:
            continue
    elif a[0] == 'P':
        c.append(a[1])
print(''.join(c + list(reversed(c2))))
# 스택을 이용한 풀이, 다시 풀어풀 수 있도록
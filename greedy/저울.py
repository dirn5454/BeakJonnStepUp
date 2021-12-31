n = int(input())
nlist = list(map(int, input().split()))
nlist.sort()
number = 1
for i in range(n):
    if number >= nlist[i]:
        number += nlist[i]
    else:
        break
print(number)

# 다시 문제 이해
# 풀이가 이해 X
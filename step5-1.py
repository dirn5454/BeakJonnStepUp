a = int(input())
num = list(map(int, input().split()))

max_num = num[0]
min_num = num[0]
for i in num:
    if max_num < i:
        max_num = i
    if min_num > i:
        min_num = i

print(min_num, max_num)    


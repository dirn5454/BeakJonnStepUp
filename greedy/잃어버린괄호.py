# n = input().split('-')
# count = 0
# if len(n) == 1:
#     count = eval(n[0])
# else:
#     for i in range(len(n)):
#         if '+' not in n[i] and i == 0:
#             count = int(n[i])
#         elif '+' not in n[i]:
#             count -= int(n[i])
#         elif '+' in n[i]:
#             count -= eval(n[i])
# print(count)

n = input().split('-')
count = 0
for i in n[0].split('+'):
    count += int(i)
for i in n[1:]:
    for j in i.split('+'):
        count -= int(j)
print(count)
# split()을 잘 활용할 것
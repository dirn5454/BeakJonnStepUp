# n1 = input()
# n2 = input()
# print(n1.count(n2))

n1 = input()
n2 = input()
count = 0
check_len = len(n2)
for_len = len(n1)//len(n2)
for i in range(for_len):
    if n2 == n1[i:check_len+i]:
        count += 1
print(count)
s = input()
zcount = 0
ocount = 0
for i in range(len(s)):
    s = s.replace('11', '1')
    s = s.replace('00', '0')
zcount = s.count('0')
ocount = s.count('1')
print(min(zcount, ocount))

# 다른 정답 바뀌는 횟수를 count
# s= input()
# count = 0
# for i in range(len(s)-1):
#     if s[i] != s[i+1]:
#         count += 1
# print((count+1)//2)
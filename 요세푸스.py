# 내 풀이
a,b = map(int, input().split())
nlist=[]
for i in range(1,a+1):
    nlist.append(i)
print('<',end='')
r = b
while len(nlist) != 0:
    if b > len(nlist):
        b -= len(nlist)
    else:
        if len(nlist) == 1:
            print(nlist.pop(b-1), end='')
        else:
            print(nlist.pop(b-1), end=', ')
        b += r-1
print('>')

# n, k = map(int, input().split())
# arr = [i for i in range(1, n + 1)]
# answer = []
# num = k - 1

# for i in range(n):
#     if len(arr) > num:
#         answer.append(arr.pop(num))
#         num += k - 1
#     elif len(arr) <= num:
#         num = num % len(arr)
#         answer.append(arr.pop(num))
#         num += k -1
        
# print("<", ', '.join(str(i) for i in answer), ">", sep = '')
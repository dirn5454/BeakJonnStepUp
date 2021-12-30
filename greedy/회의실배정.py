# 시간초과
# import sys
# n = int(sys.stdin.readline())
# nlist = []
# count_list = []
# for i in range(1,n+1):
#     nlist.append(list(map(int, sys.stdin.readline().split())))
# nlist.sort()
# while len(nlist) > 1:
#     count = 0
#     clist = []
#     for i in range(len(nlist)):
#         if len(clist) == 0 or clist[-1] <= nlist[i][0]:
#             clist.append(nlist[i][1])
#             count += 1
#     count_list.append(count)
#     nlist.pop(0)
# print(max(count_list))
# 다시 풀어보기
import heapq
n = int(input())
nlist = []
for i in range(n):
    nlist.append(list(map(int, input().split())))
nlist.sort()
h = []
heapq.heappush(h, nlist[0][1])
for i in range(1,len(nlist)):
    if h[0] > nlist[i][0]:
        heapq.heappush(h, nlist[i][1])
    else:
        heapq.heappop(h)
        heapq.heappush(h, nlist[i][1])
print(len(h))
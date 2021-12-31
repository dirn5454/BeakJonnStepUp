# heap은 기본적으로 min
import heapq
n,m = map(int, input().split())
heap = []
nlist = list(map(int, input().split()))
for i in nlist:
    heapq.heappush(heap, i)
for i in range(m):
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    heapq.heappush(heap, num1+num2)
    heapq.heappush(heap, num1+num2)
print(sum(heap))
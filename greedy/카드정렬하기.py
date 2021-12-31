import heapq
n = int(input())
heap = []
number = 0
for i in range(n):
    heapq.heappush(heap, int(input()))
while len(heap) != 1:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    number += num1+num2
    heapq.heappush(heap, num1+num2)
print(number)
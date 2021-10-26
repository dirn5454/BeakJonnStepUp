t = int(input())
for i in range(t):
    k = int(input()) # 층
    n = int(input()) # 호
    k_num = [j for j in range(1, n+1)]
    # result = k-1층의 n호 까지의 수 
    # f1의 2호이면 f0의 1호 2호
    for x in range(k):
        for y in range(1, n):
            k_num[y] += k_num[y-1] # 
print(k_num[-1])
n = int(input())
m = list(map(int,input().split()))
max_m = max(m)
for i in range(len(m)):
    m[i] = m[i]*100/max_m
print(sum(m)/len(m))
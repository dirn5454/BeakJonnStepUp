# 다시 풀어볼듯 스스로
n = int(input())
rlist = list(map(int, input().split()))
clist = list(map(int, input().split()))
clist.pop()
cost = clist[0]*rlist[0]
min_cost = clist[0]
for i in range(len(clist)-1):
    if min_cost < clist[i+1]:
        cost += min_cost*rlist[i+1]
    else:
        min_cost = clist[i+1]
        cost += min_cost*rlist[i+1]
print(cost)
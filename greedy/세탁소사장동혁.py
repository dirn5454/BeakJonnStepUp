n = int(input())
for i in range(n):
    num = int(input())
    q = num//25
    num -= (num//25)*25
    d = num//10
    num -= (num//10)*10
    n = num//5
    num -= (num//5)*5
    p = num//1
    num -= (num//1)*1
    print(q,d,n,p)
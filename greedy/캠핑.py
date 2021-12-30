l,p,v = map(int, input().split())
i = 1
while l!=0 and p != 0 and v != 0:
    count = 0
    count += (v//p)*l
    v -= (v//p)*p
    if v <= l: # 남은 휴가일이 사용가능일보다 작거나 같을때
        count += v
    else: # 남은 휴가일이 사용가능일보다 클 떄
        count += l
    print('Case '+ str(i) +': '+ str(count))
    i += 1
    l,p,v = map(int, input().split())
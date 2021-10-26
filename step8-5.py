num = int(input())
for i in range(num):
    h,w,n = map(int, input().split())
    if n%h ==0:
        floor = h
        number =  n//h
    else:
        floor = n%h
        number =  n//h+1
    print(floor*100+number)
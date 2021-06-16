from typing import NamedTuple


N = int(input())
A = N
count =0
while 1:
    N = (N%10)*10 + (N//10 + N%10)%10
    count+=1
    if(A == N):
        print(count)
        break

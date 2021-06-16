import sys
T = int(input())

for x in range(1, T+1):
    A,B= map(int, sys.stdin.readline().split())
    print("Case #",x,":", A+B)




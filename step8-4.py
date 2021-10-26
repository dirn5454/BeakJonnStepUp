import math
a,b,c = map(int, input().split())
day = (c-b)/(a-b)
print(math.ceil(day))
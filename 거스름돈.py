n = int(input())
n = 1000-n
count = 0

if n>500:
    count += n//500
    n = n%500
if n>100:
    count += n//100
    n = n%100
if 100>n>49:
    count += n//50
    n = n%50
if 50>n>9:
    count += n//10
    n = n%10
if 10>n>5:
    count += n//5
    n = n%5
if 5>n>0:
    count += n//1
    n = 0   
print(count)

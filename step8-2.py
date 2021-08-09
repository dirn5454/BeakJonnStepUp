num = int(input())
start=1
count = 1
while num > start:
    start = start +6*count
    count += 1
print(count)
arr = []
for i in range(10):
    n = int(input())
    arr.append(n%42)
s = set(arr)
print(len(s))

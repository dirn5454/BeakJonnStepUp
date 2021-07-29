a,b = input().split()
a = "".join(reversed(a))
b = "".join(reversed(b))
if int(a) > int(b):
    print(a)
if int(a) < int(b):
    print(b)
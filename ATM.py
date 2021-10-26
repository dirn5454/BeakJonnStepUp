n = int(input())
plist = list(map(int, input().split()))
plist.sort()
plist.reverse()
psum = 0
for i in range(len(plist)):
    psum += sum(plist)
    plist.pop(0)
print(psum)
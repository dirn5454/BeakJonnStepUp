H, M = input().split()
H = int(H)
M = int(M)

if(M-45>0):
    if(H==0):
        print(23, M-45)
    else:
        print(H-1, M-45)
else:
    if(H==0):
        print(23, M+15)
    else:
        print(H-1, M+15)
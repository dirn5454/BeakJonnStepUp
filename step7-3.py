s = input()
for i in range(97,123):
    if chr(i) not in s:
        print(-1)
    else:
        print(s.index(chr(i)))
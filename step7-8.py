word = input()
count = 0
for i in word:
    if 64 < ord(i) < 68:
        count += 3
    elif 67 < ord(i) < 71:
        count += 4
    elif 70 < ord(i) < 74:
        count += 5
    elif 73 < ord(i) < 77:
        count += 6
    elif 76 < ord(i) < 80:
        count += 7
    elif 79 < ord(i) < 84:
        count += 8
    elif 83 < ord(i) < 87:
        count += 9
    elif 86 < ord(i) < 91:
        count += 10
print(count)
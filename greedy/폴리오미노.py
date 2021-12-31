n = input()
if 'XXXX' in n:
    n = n.replace('XXXX', 'AAAA')
if 'XX' in n:
    n = n.replace('XX', 'BB')
if 'X' in n:
    n = -1
print(n)

# n = input()
# n = n.replace('XXXX', 'AAAA')
# n = n.replace('XX', 'BB')
# if 'X' in n:
#     n = -1
# print(n)
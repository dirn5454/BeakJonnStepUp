n = int(input())
ch = input()
if 'S' in ch:
    ch = ch.replace('S','*S*')
if 'LL' in ch:
    ch = ch.replace('LL','*LL*')
if '**' in ch:
    ch = ch.replace('**','*')
if 'LL' in ch:
    print(ch.count('*'))
else:
    print(ch.count('*')-1)

# n = int(input())
# ch = input()
# count = ch.count('LL')
# if count <= 1:
#     print(len(ch))
# else:
#     print(len(ch)-count+1)
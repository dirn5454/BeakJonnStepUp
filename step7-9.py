c = input()
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in a:
    c = c.replace(i, '*')
print(len(c))
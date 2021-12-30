n = int(input())
clist = []
for i in range(n):
    count = 0
    t = input()
    for i in t:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            print('NO')
            break
# 0보다 큰수라고 명확히 선언해주는 이유는 위에서 
# 0보다 작은것은 NO를 이미 출력했기 때문에 
# 0이 아닌 것이라 명시할 경우 NO가 두 번 출력됨       
    if count > 0: 
        print('NO')
    elif count == 0:
        print('YES')
n,m,v = map(int, input().split())
num_list=[]
num_list.append([])
for i in range(1, m+1):
    m_list = list(map(int, input().split()))
    num_list.append(m_list)
print(num_list)
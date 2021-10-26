from collections import deque
n,m,v = map(int, input().split())
graph = [[0]*(n+1) for i in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def bfs(v):
    #방문할 곳을 순서대로 넣을 큐
    queue = [v]
    # 방문체크
    visited[v] = 1
    #큐안에 데이터가 없을 때까지
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 1
bfs(v)
# 이해 필요
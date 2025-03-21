import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def BFS():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q = deque()

    for i in range(n):
        for j in range(m):
            if Graph[i][j] == 1:
                Q.append((i, j))

    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if Graph[nx][ny] == 0:
                    Graph[nx][ny] = Graph[x][y] + 1
                    Q.append((nx, ny))
    

Graph = []   
m, n = map(int, input ().split())
for _ in range(n):
    a = list(map(int, input().split()))
    Graph.append(a)

BFS()

ans = 0
for i in range(n):
    if 0 in Graph[i]:
        print(-1)
        quit()
    ans = max(ans, max(Graph[i]))

print(ans-1)
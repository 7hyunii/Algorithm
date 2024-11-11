import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def BFS(x, y):
    max_cnt = 0
    visited[x][y] = 1
    Q = deque()
    Q.append([x, y, 0])

    while Q:
        x, y, cnt = Q.popleft()
        if max_cnt < cnt:
            max_cnt = cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and Graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                Q.append([nx, ny, cnt+1])
                visited[nx][ny] = 1

    return max_cnt

n, m = map(int, input().split())
Graph = [list(input().rstrip()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maxx = -1
for i in range(n):
    for j in range(m):
        if Graph[i][j] == 'L':
                visited = [[0]*m for _ in range(n)]
                maxx = max(BFS(i, j), maxx) 

print(maxx)
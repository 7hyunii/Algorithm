import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def BFS(x, y):
    cnt = 1
    visited[x][y] = 1
    Q = deque()
    Q.append([x, y])

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and Graph[nx][ny] == '1' and visited[nx][ny] == 0:
                Q.append([nx, ny])
                visited[nx][ny] = 1
                cnt += 1

    return cnt

n = int(input())
Graph = [list(input().rstrip()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*n for _ in range(n)]
ans = []

for i in range(n):
    for j in range(n):
        if Graph[i][j] == '1' and visited[i][j] == 0:
                ans.append(BFS(i, j))

ans.sort()
print(len(ans), *ans, sep="\n")
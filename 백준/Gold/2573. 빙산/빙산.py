import sys
input = sys.stdin.readline
from collections import deque

dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)


def bfs(x, y):
    dq = deque([(x, y)])
    visited.add((x, y))

    while dq:
        x, y = dq.popleft() 
        cnt = 0

        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    cnt += 1

                elif graph[nx][ny] > 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dq.append((nx, ny))
        
        if cnt > 0:
            note.append((x, y, cnt))


ans = 0
while 1:
    visited = set()
    note = []
    check = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and (i, j) not in visited:
                bfs(i, j)
                check += 1
    
    if check >= 2:
        print(ans)
        break
    elif check == 0:
        print(0)
        break
            
    for x, y, cnt in note:
        graph[x][y] = graph[x][y] - cnt if graph[x][y] - cnt > 0 else 0

    ans += 1



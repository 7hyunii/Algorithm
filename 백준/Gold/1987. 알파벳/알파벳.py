import sys
input = sys.stdin.readline

def DFS(x, y, depth):
    visited[Graph[x][y]] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < r) and (0 <= ny < c):
            if visited[Graph[nx][ny]] != 1:                         
                visited[Graph[nx][ny]] = 1
                DFS(nx, ny, depth+1)
                visited[Graph[nx][ny]] = 0
                
    visited[Graph[x][y]] = 0
    ans.add(depth)
    

r, c = map(int, input().split())
Graph = [list(map(lambda x:ord(x)-65, input().rstrip())) for _ in range(r)]
visited = [0] * 26
ans = set()

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
DFS(0, 0, 1)
print(max(ans))
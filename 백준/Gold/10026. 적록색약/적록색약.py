import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def DFS(x, y, color, check):    #check = 정상 or 적록색약 판단
    if check==1:
        visited1[x][y]=1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx <n) and (0 <= ny < n) and visited1[nx][ny]==0:
                if Graph1[nx][ny]==color:
                    DFS(nx, ny, color, 1)
    else:
        visited2[x][y]=1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx <n) and (0 <= ny < n) and visited2[nx][ny]==0:
                if Graph2[nx][ny]==color:
                    DFS(nx, ny, color, 0)

n = int(input())
Graph1 = [list(input().rstrip()) for _ in range(n)]
Graph2 = copy.deepcopy(Graph1)                          #2차원배열 깊은복사
for i in range(n):
    for j in range(n):
        if Graph1[i][j]=='G':
            Graph2[i][j]='R'

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited1 = [[0]*n for _ in range(n)]
visited2 = [[0]*n for _ in range(n)]
normal = 0
rg_m = 0

for color in ['R', 'G', 'B']:
    for i in range(n):
        for j in range(n):
            if  Graph1[i][j]==color and visited1[i][j]==0:
                DFS(i, j, color, 1)
                normal+=1

            if  Graph2[i][j]==color and visited2[i][j]==0:
                DFS(i, j, color, 0)
                rg_m+=1

print(normal, rg_m)
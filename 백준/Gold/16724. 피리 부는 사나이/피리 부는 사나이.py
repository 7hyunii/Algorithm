import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

n, m = map(int, input().split())
Graph = [input().strip() for _ in range(n)]
parent = [i for i in range(n * m)]

dir = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
for i in range(n):
    for j in range(m):
        cur = i * m + j             # 현재 좌표 (i, j)를 1차원 인덱스로 변환
        di, dj = dir[Graph[i][j]]
        ni, nj = i + di, j + dj     #다음 위치 계산
        nxt = ni * m + nj           #다음 칸의 1차원 인덱스 계산
        union(cur, nxt)             #현재 칸과 다음 칸 union

ans = set()
for i in range(n * m):
    ans.add(find(i))

#print(parent)
print(len(ans))


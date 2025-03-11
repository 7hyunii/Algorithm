import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dist = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if dist[a][k] and dist[k][b]:
                dist[a][b] = 1

#print(dist)

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if dist[i][j] == 0 and dist[j][i] == 0:
            cnt += 1
    print(cnt-1)
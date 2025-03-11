import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dist = [[float('INF')]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        dist[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            dist[a][b] = min(dist[a][b], dist[a][k]+dist[k][b])

Sum = float('INF')
ans = 0
for i in range(1, n+1):
    if Sum > sum(dist[i][1:]):
        Sum = sum(dist[i][1:])
        ans = i

print(ans)

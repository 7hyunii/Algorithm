import sys
input = sys.stdin.readline

n, m = map(int, input().split())
Graph = [[float('INF')]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    Graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            Graph[a][b] = min(Graph[a][b], Graph[a][k]+Graph[k][b])

ans = float('INF')
for i in range(1, n+1):
	for j in range(1, n+1):
		ans = min(ans, Graph[i][j]+Graph[j][i])
		
if ans == float('INF'):
	print(-1)
else:
	print(ans)
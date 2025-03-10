import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
Graph = [[float('INF')]*(n+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            Graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    Graph[a][b] = min(Graph[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            Graph[a][b] = min(Graph[a][b], Graph[a][k]+Graph[k][b])
    
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if Graph[a][b] == float('INF'):
            print(0, end=" ")
        else:
            print(Graph[a][b], end=" ")
    print()
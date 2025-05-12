import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
Graph = [[float('INF')]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    Graph[a][b] = l
    Graph[b][a] = l

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            Graph[a][b] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            Graph[i][j] = min(Graph[i][j], Graph[i][k]+Graph[k][j])

Max = 0
for i in range(1, n+1):
    Compare = 0
    for j in range(1, n+1):
        if Graph[i][j] <= m:
            Compare += items[j-1]
    if Max < Compare:
        Max = Compare

print(Max)
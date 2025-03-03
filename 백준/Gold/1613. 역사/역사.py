import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dist = [[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    dist[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if dist[a][k] and dist[k][b]:
                dist[a][b] = 1

#print(dist)

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if dist[a][b] != 0:
        print(-1)
    elif dist[b][a] != 0:
        print(1)
    else:
        print(0)
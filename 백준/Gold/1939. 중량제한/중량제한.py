import sys
input=sys.stdin.readline

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
Graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    Graph.append((c, a, b))

s, e = map(int, input().split())
Graph.sort(reverse=True)

parent = [i for i in range(n+1)]

for c, a, b in Graph:
    union(a, b)
    if find(s) == find(e):
        print(c)
        quit()
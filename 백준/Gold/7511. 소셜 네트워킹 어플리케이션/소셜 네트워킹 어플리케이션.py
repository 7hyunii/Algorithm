import sys
input=sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

T = int(input())
for t in range(1, T+1):
    n = int(input())
    parent = [i for i in range(n+1)]

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)

    k = int(input())
    print(f"Scenario {t}:")
    for _ in range(k):
        u, v = map(int, input().split())
        if find(u) == find(v):
            print(1)
        else:
            print(0)
    print()
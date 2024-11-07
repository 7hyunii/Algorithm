import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**7)

def DFS(start, end, v):
    global d
    visited.add(start)
    if start == end:
        print(v)
        return 

    for node, vol in Graph[start]:
        if node not in visited:
            DFS(node, end, v + vol)

n, m = map(int, input().split())
Graph = defaultdict(list)
for _ in range(n-1):
    a, b, c = map(int, input().split())
    Graph[a].append([b, c])
    Graph[b].append([a, c])

for _ in range(m):
    a, b = map(int, input().split())
    visited = set()
    DFS(a, b, 0)
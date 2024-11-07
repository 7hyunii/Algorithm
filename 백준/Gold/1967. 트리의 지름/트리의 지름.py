import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**7)

def DFS(start, v):
    for a, c in Graph[start]:
        if vol[a] == -1:
            vol[a] = c + v
            DFS(a, vol[a])

n = int(input())
Graph = defaultdict(list)
for _ in range(n-1):
    a, b, c = map(int, input().split())
    Graph[a].append([b, c])
    Graph[b].append([a, c])

vol = [-1] * (n+1)
vol[1] = 0
DFS(1, 0)
#print(vol)

node = vol.index(max(vol))
vol = [-1] * (n+1)
vol[node] = 0
DFS(node, 0)
#print(vol)

print(max(vol))
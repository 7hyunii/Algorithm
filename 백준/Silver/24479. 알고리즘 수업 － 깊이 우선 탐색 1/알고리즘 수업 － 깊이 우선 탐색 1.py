import sys
input = sys.stdin.readline
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)

def DFS(start):
    global cnt
    visited[start] = cnt

    for node in Graph[start]:
        if not visited[node]:
            cnt += 1
            DFS(node)


Graph = defaultdict(list)
n, m, r = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    Graph[a].append(b)
    Graph[b].append(a)

for key in Graph:
    Graph[key].sort()

visited = [0] * (n+1)
cnt = 1
DFS(r)

print(*visited[1:], sep="\n")
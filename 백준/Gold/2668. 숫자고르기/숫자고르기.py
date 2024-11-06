import sys
input=sys.stdin.readline
from collections import defaultdict

Graph = defaultdict(list)
def DFS(start, visited=[]):
    visited.append(start)
    for i in Graph[start]:
        if i not in visited:
            DFS(i, visited)
        if visited[0] == i:
            ans.extend(visited)

n = int(input())
for i in range(1, n+1):
    Graph[i].append(int(input()))

ans = []
for i in range(1, n+1):
    DFS(i, visited=[])

ans = sorted(set(ans))
print(len(ans), *ans, sep="\n")
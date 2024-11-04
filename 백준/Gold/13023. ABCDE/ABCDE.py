import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**7)

Graph = defaultdict(list)

def DFS(start, depth, visited=set()):
    if depth == 4:
        print(1)
        quit()

    visited.add(start)
    for i in Graph[start]:
        if i not in visited:
            DFS(i, depth+1, visited)
    visited.remove(start)

N, M = map(int, input().split())
for _ in range(M):
    a, b = map(int, input().split())
    Graph[a].append(b)
    Graph[b].append(a)

for i in range(N):
    DFS(i, 0)

print(0)
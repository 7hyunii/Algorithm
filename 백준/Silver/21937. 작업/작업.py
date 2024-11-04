import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**7)

Graph = defaultdict(list)

def DFS(start, visited=set()):
    visited.add(start)
    for i in Graph[start]:
        if i not in visited:
            DFS(i, visited)
    return visited


N, M = map(int, input().split())
for _ in range(M):
    a, b = map(int, input().split())
    Graph[b].append(a)

X = int(input())

print(len(DFS(X))-1)
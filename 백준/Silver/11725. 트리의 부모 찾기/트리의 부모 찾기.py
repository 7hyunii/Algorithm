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
            ans[i] = start

n = int(input())
ans = [0]*(n+1)
for i in range(n-1):
    a, b = map(int, input().split())
    if a==1:
        Graph[a].append(b)
    elif b==1:
        Graph[b].append(a)
    else:
        Graph[a].append(b)
        Graph[b].append(a)

DFS(1)
print(*ans[2:], sep="\n")
import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**7)

def DFS(v, c):
    color[v] = c
    for node in Graph[v]:
        if node not in color:
            if not DFS(node, 1-c):
                return False
        elif color[node] == color[v]:
            return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    Graph = defaultdict(list)
    for _ in range(e):
        a, b = map(int, input().split())
        Graph[a].append(b)
        Graph[b].append(a)

    color = dict()
    Check = True

    for node in range(1, v+1):
        if node not in color:
            if not DFS(node, 0):
                Check = False
                break

    if Check:
        print("YES")
    else:
        print("NO")
import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def BFS(start):
    distances[start] = 0
    visited = set()
    visited.add(start)

    Q = deque()
    Q.append(start)
    
    while Q:
        v = Q.popleft()

        for node in Graph[v]:
            if node not in visited:
                visited.add(node)
                Q.append(node)
                distances[node] = distances[v] + 1
   
Graph = defaultdict(list)
n, m, k, x = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    Graph[a].append(b)

#print(Graph)
distances = [-1] * (n+1)
BFS(x)

if k not in distances:
    print(-1)
else:
    for i in range(1, n+1):
        if distances[i] == k:
            print(i)
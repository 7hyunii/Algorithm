import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def BFS(s):
    dist = [-1] * (n+1)
    dist[s] = 0
    Q = deque([s])

    while Q:
        v = Q.popleft()

        for node in Graph[v]:
            if dist[node] == -1:
                dist[node] = dist[v] + 1
                Q.append(node)

    return dist

Graph = defaultdict(list)
n, m, q = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    Graph[b].append(a)

for _ in range(q):
    u, v = map(int, input().split())
    dist_u = BFS(u)
    dist_v = BFS(v)
    #print(dist_u, dist_v)
    
    ans = float('inf')
    for x in range(1, n+1):
        if dist_u[x] != -1 and dist_v[x] != -1:
            ans = min(ans, max(dist_u[x], dist_v[x]))
    
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
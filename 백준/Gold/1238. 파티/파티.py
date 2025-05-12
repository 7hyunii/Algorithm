import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict
Graph = defaultdict(list)

n, m, x = map(int, input().split())
for _ in range(m):
    a, b, c = map(int, input().split())
    Graph[a].append((c, b))

def Dijk(k):
    dist = [float('INF')] * (n+1)
    dist[k] = 0
    heap = [(0, k)]

    while heap:
        weight, node = heapq.heappop(heap)

        if dist[node] < weight:
            continue

        for n_weight, neighbor in Graph[node]:
            n_dist = weight + n_weight
            if n_dist < dist[neighbor]:
                dist[neighbor] = n_dist
                heapq.heappush(heap, (n_dist, neighbor))
    
    return dist


comebackhome = Dijk(x)

ans = 0
for i in range(1, n+1):
    if i != x:
        go = Dijk(i)[x]
        ans = max(ans, go + comebackhome[i])

print(ans)
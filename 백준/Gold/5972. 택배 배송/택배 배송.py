import sys
input = sys.stdin.readline
from collections import defaultdict
import heapq

n, m = map(int, input().split())
Graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    Graph[a].append((c, b))
    Graph[b].append((c, a))

dist = [float('inf')] * (n+1)
dist[1] = 0
heap = [(0, 1)]
while heap:
    weight, node = heapq.heappop(heap)

    if dist[node] < weight:
            continue

    for next_weight, next_node in Graph[node]:
        next_dist = next_weight + weight
        if next_dist < dist[next_node]:
            dist[next_node] = next_dist
            heapq.heappush(heap, (next_dist, next_node))

print(dist[n])
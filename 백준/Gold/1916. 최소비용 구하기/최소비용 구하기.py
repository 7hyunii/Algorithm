import heapq
from collections import defaultdict

def Dijk(x, y):
    dist = [float('inf')] * (n+1)
    dist[x] = 0
    heap = [(0, x)]

    while heap:
        weight, node = heapq.heappop(heap)

        if dist[node] < weight:
            continue

        for n_weight, neighbor in Graph[node]:
            n_dist = weight + n_weight
            if n_dist < dist[neighbor]:
                dist[neighbor] = n_dist
                heapq.heappush(heap, (n_dist, neighbor))

    return dist[y]

Graph = defaultdict(list)
n = int(input())
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    Graph[a].append((c, b))

x, y = map(int, input().split())

#print(Graph)
print(Dijk(x, y))
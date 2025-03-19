import heapq
from collections import defaultdict

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

Graph = defaultdict(list)
n, m = map(int, input().split())
k = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    Graph[a].append((c, b))

ans = Dijk(k)[1:]
for i in ans:
    if i == float('INF'):
        print("INF")
    else:
        print(i)
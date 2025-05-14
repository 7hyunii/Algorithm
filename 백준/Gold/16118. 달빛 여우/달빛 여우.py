import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict
Graph = defaultdict(list)

n, m= map(int, input().split())
for _ in range(m):
    a, b, d = map(int, input().split())
    Graph[a].append((d*2, b))
    Graph[b].append((d*2, a))

def Dijk_Fox(k):
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

def Dijk_Wolf(k):
    dist = [[float('INF')]*2 for _ in range(n+1)]
    dist[k][1] = 0
    heap = [(0, k, 1)]

    while heap:
        weight, node, Tog = heapq.heappop(heap)

        if dist[node][Tog] < weight:
            continue

        for n_weight, neighbor in Graph[node]:
            if Tog == 1:
                n_dist = weight + n_weight//2
                if n_dist < dist[neighbor][0]:
                    dist[neighbor][0] = n_dist
                    heapq.heappush(heap, (n_dist, neighbor, 0))
            else:
                n_dist = weight + n_weight*2
                if n_dist < dist[neighbor][1]:
                    dist[neighbor][1] = n_dist
                    heapq.heappush(heap, (n_dist, neighbor, 1))
    return dist


Fox = Dijk_Fox(1)
Wolf = Dijk_Wolf(1)

ans = 0
for i in range(2, n+1):
    if Fox[i] < min(Wolf[i][0], Wolf[i][1]):
        ans += 1

print(ans)
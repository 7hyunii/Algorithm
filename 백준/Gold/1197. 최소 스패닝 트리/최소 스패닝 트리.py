import heapq
from collections import defaultdict

def Prim():
    dist = 0
    visited = set()
    heap = [(0, 1)]

    while heap:
        weight, node = heapq.heappop(heap)
        
        if node not in visited:
            visited.add(node)
            dist += weight

            for n_weight, neighbor in Graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (n_weight, neighbor))

    return dist

Graph = defaultdict(list)
n, m = map(int, input().split())
for _ in range(m):
    a, b, c = map(int, input().split())
    Graph[a].append((c, b))
    Graph[b].append((c, a))

#print(Graph)
print(Prim())
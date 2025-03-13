import sys, heapq
input = sys.stdin.readline

heap = []   
n = int(input())
for _ in range(n):
    m = int(input())
    heapq.heappush(heap, m)

ans = 0
while len(heap) > 1:
    k1 = heapq.heappop(heap)
    k2 = heapq.heappop(heap)
    ans += k1 + k2
    heapq.heappush(heap, k1 + k2)

print(ans)
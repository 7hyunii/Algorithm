import sys
input = sys.stdin.readline
import heapq

n = int(input())
for _ in range(n):
    T = int(input())
    heap = list(map(int, input().split()))
    ans = 0

    heapq.heapify(heap)
    #print(heap)
    
    while len(heap) > 1:
        k1 = heapq.heappop(heap)
        k2 = heapq.heappop(heap)
        heapq.heappush(heap, k1+k2)
        ans +=  k1 + k2
        #print(ans)

    print(ans)
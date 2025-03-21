import sys, heapq
input = sys.stdin.readline

heap1, heap2 = [], []
n, m, k = map(int, input().split())
for _ in range(k):
    v, p = map(int, input().split())
    heap1.append((p, v))

heap1.sort()

vSum = 0
for p, v in heap1:
    heapq.heappush(heap2, v)
    vSum += v

    if len(heap2) > n:
        vSum -= heapq.heappop(heap2)

    if len(heap2) == n and vSum >= m:
        print(p)
        quit()

    #print(heap2)
        
print(-1)
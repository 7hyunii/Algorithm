import sys
input = sys.stdin.readline
import heapq

n = int(input())

arr = []
for _ in range(n):
    p, d = map(int, input().split())
    arr.append((d, p))
arr.sort()
#print(arr)

heap = []
for d, p in arr:
    heapq.heappush(heap, p)

    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))


# 1 : 20, 2
# 2 : 100, 8
# 3 : 10
# 10 : 50
# 20 : 5

# 185
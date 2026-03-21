import sys
input = sys.stdin.readline
import heapq

n = int(input())

arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))
arr.sort()
#print(arr)

heap = []
heapq.heappush(heap, arr[0][1])
for i in range(1, n):
    if arr[i][0] < heap[0]:
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])

print(len(heap))  


# 1 3
# 2 4
# 3 5
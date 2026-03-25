import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []
for _ in range(n):
    h, o = map(int, input().split())
    arr.append((min(h, o), max(h, o)))
arr.sort(key=lambda x: x[1])
#print(arr)
d = int(input())

heap = []
ans = 0
for start, end in arr:
    if end - start <= d:
        heapq.heappush(heap, start)
        while heap:
            if end - d > heap[0]:
                heapq.heappop(heap)
            else:
                break
            
        ans = max(ans, len(heap))

print(ans)

"""
abs(h-o) > d :  Delete

40 20 25 30 35 50 60 100
25

"""
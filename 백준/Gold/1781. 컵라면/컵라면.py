import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()
#print(arr)

heap = []

for i in range(n):
    heapq.heappush(heap, arr[i][1])

    if len(heap) > arr[i][0]:
        heapq.heappop(heap)


print(sum(heap))


"""
1: 6, 7
2: 4, 5
3: 2, 1
6: 1

"""
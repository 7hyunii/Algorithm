import sys, heapq
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    a = map(int, input().split())
    for i in a:
        if len(heap) < n:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappushpop(heap, i)

#print(heap)
print(heap[0])
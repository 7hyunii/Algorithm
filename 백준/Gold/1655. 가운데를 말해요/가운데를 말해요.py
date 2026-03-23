import sys
input = sys.stdin.readline
import heapq

n = int(input())
small = []
big = []
for i in range(n):
    a = int(input())

    if len(small) == len(big):
        heapq.heappush(small, (-a, a))
    else:
        heapq.heappush(big, a)

    if small and big:
        if small[0][1] > big[0]:
            s = heapq.heappop(small)[1]
            b = heapq.heappop(big)
            heapq.heappush(small, (-b, b))
            heapq.heappush(big, s)

    print(small[0][1])

# 1 5 2 10 7 5
# 10 2 1
# 5 7
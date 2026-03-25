import sys
input = sys.stdin.readline
import heapq

k, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

primal = arr[:]
heapq.heapify(arr)
for _ in range(n):
    num = heapq.heappop(arr)
    for p in primal:
        heapq.heappush(arr, num*p)
        if num % p == 0:
            break

print(num)

"""
2 3 5 7

중복제거?
set => 메모리 초과

"""

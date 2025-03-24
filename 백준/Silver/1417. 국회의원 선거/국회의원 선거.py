import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []
for i in range(n):
	a = int(input())
	if i == 0:
		Dasom = a
	else:
		heapq.heappush(arr, (-a, a))

cnt = 0
while arr:
	n = heapq.heappop(arr)[1]
	if n >= Dasom:
		n -= 1
		Dasom += 1
		heapq.heappush(arr, (-n, n))
		cnt += 1

print(cnt)
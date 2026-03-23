import sys
input = sys.stdin.readline
import heapq

T = int(input())
for _ in range(T):
	m = int(input())
	arr = []
	while len(arr) < m:
		arr.extend(map(int, input().split()))

	ans = []
	small = []
	big = []
	for i in range(m):
		if len(small) == len(big):
			heapq.heappush(small, -arr[i])
		else:
			heapq.heappush(big, arr[i])
		
		if small and big and -small[0] > big[0]:
			a = -heapq.heappop(small)
			b = heapq.heappop(big)
			heapq.heappush(small, -b)
			heapq.heappush(big, a)
			
		if i % 2 == 0:
			ans.append(-small[0])

	print(m//2+1)
	for i in range(0, m//2+1, 10):
		print(*ans[i:i+10])
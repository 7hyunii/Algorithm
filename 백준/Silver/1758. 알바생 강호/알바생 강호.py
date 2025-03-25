import sys
input = sys.stdin.readline

n = int(input())
arr = []
ans = 0
for _ in range(n):
	a = int(input())
	arr.append(a)
	
arr.sort(reverse=True)
for i in range(n):
	if arr[i] - i > 0:
		ans += arr[i] - i

print(ans)
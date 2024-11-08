import sys
input=sys.stdin.readline
from collections import deque

n = int(input())
arr = list(map(int, input().split()))
ans = [-1] * n
d = deque()

for i in range(n):
    while d and arr[d[-1]] < arr[i]:
        ans[d.pop()] = arr[i]
    d.append(i)

print(*ans)
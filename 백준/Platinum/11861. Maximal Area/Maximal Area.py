import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = list(map(int, input().split())) + [0] 

stack = []
ans = 0
for i in range(n+1):
    while stack and arr[stack[-1]] > arr[i]:
        h = arr[stack.pop()]

        if stack:
            l = stack[-1]
        else:
            l = -1

        ans = max(ans, h * (i-l-1))
    
    stack.append(i)

print(ans)

import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))

stack = []
ans = [0] * n
for i in range(n):
    while stack and stack[-1][0] <= t[i]:
        stack.pop()

    if stack:
        ans[i] = stack[-1][1]

    stack.append((t[i], i+1))

print(*ans)
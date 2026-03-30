import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)] + [0]
stack = []
ans = 0

for i in range(n+1):
    while stack and arr[stack[-1]] > arr[i]:
        h = arr[stack.pop()]

        if not stack:
            w = i
        else:
            w = i - stack[-1] - 1

        ans = max(ans, h*w)
    
    stack.append(i)


print(ans)

"""
2 1 4 5 1 3 3

"""
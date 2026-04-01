import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
ans = 0
for i in range(n):
    while stack and stack[-1] <= arr[i]:
        x = stack.pop()

        if stack:
            if stack[-1] < arr[i]:
                ans += stack[-1] - x
            else:
                ans += arr[i] - x
        else:
            ans += arr[i] - x
    
    stack.append(arr[i])
    # print(stack, ans)

if len(stack) > 1:
    ans += stack[0] - stack[-1]

print(ans)

"""
3 2 5 4 1

stack
3 2
5       5-2   
5 4 1  
        5-1

"""
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
ans = 0
for i in range(n):
    cnt = 1

    while stack and stack[-1][0] < arr[i]:
        ans += stack[-1][1]
        stack.pop()

    if stack and stack[-1][0] == arr[i]:
        cnt = stack.pop()[1]
        ans += cnt
        cnt += 1

        if stack:
            ans += 1

    elif stack:
        ans += 1
    
    stack.append((arr[i], cnt))
    # print(stack, i, ans)       
    
print(ans)

"""
2 4 1 2 2 5 1

2
2 4     +1
4
4 1     +2
4 2     +4
4 2 2   +6 !!
5       +9
5       +10


"""
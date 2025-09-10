#22866
import sys
input = sys.stdin.readline

n = int(input())
H = list(map(int, input().split()))

cnt = [0] * (n+1)
see = [0] * (n+1)
# Left -> Right
stack = []
for i in range(1, n+1):
    while stack and stack[-1][0] <= H[i-1]:
        stack.pop()
    cnt[i] = len(stack)

    if stack:
        see[i] = stack[-1][1]

    stack.append([H[i-1], i])

# Right -> Left
stack = []
for i in range(n, 0, -1):
    while stack and stack[-1][0] <= H[i-1]:
        stack.pop()
    cnt[i] = cnt[i] + len(stack)

    if stack:
        if see[i] == 0:
            see[i] = stack[-1][1]
        else:
            if abs(i - stack[-1][1]) == abs(i - see[i]):
                see[i] = min(stack[-1][1], see[i])
            elif abs(i - stack[-1][1]) < abs(i - see[i]):
                see[i] = stack[-1][1]

    stack.append([H[i-1], i])

#print(cnt)
#print(see)
for i in range(1, n+1):
    if cnt[i] == 0:
        print(0)
    else:
        print(cnt[i], see[i])
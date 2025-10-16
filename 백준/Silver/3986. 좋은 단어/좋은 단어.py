n = int(input())
cnt = 0
for _ in range(n):
    s = input().rstrip()
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if not stack:
        cnt += 1

print(cnt)
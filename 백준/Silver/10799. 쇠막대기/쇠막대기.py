import sys
input=sys.stdin.readline

s = input().rstrip()
stack = []
cnt = 0
prev = ""
for i in s:
    if i == "(":
        stack.append(i)
    else:
        if prev == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
    prev = i

print(cnt)
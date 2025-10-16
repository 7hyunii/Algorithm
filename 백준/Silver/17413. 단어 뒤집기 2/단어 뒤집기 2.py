import sys
input=sys.stdin.readline

s = input().rstrip()
stack = []
ans = []
check = True
for i in s:
    if i == "<":
        while stack:
            ans.append(stack.pop())
        check = False
        ans.append(i)
    elif i == ">":
        check = True
        ans.append(i)

    elif not check:
        ans.append(i)
    else:
        if i == " ":
            while stack:
                ans.append(stack.pop())
            ans.append(i)
        else:
            stack.append(i)

while stack:
    ans.append(stack.pop())

print(*ans, sep="")
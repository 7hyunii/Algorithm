import sys
input = sys.stdin.readline

s = input().strip()
stack = []
ans = 0
num = 1

for i in range(len(s)):
    if s[i] == "(":
        num *= 2
        stack.append(s[i])

    elif s[i] == "[":
        num *= 3
        stack.append(s[i])

    elif s[i] == ")":
        if not stack or stack[-1] != "(":
            print(0)
            exit()

        if s[i-1] == "(":
            ans += num

        stack.pop()
        num //= 2

    elif s[i] == "]":
        if not stack or stack[-1] != "[":
            print(0)
            exit()

        if s[i-1] == "[":  
            ans += num
            
        stack.pop()
        num //= 3

if stack:
    print(0)
else:
    print(ans)
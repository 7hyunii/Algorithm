import sys
input=sys.stdin.readline

n = int(input())
s = input().rstrip()
values = [int(input()) for _ in range(n)]

ans = 0
stack = []
for i in s:
    if 'A' <= i <= 'Z':
        stack.append(values[ord(i) - 65])
    elif i == "*":
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)

    elif i == "+":
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)

    elif i == "-":
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)

    elif i == "/":
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)

print(f"{stack[0]:.2f}")

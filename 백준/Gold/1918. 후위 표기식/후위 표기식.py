import sys
input=sys.stdin.readline
from collections import deque

n = input().rstrip()
stack = []
ans = []

for i in n:
    if i.isalpha():
        ans.append(i)
    else:
        if i == '(':
            stack.append(i)

        if i == ')':
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()

        if i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                ans.append(stack.pop())
            stack.append(i)

        if i == '+' or i == '-':
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            stack.append(i)

stack = stack[::-1]
#print(stack)        
#print(ans)
print(*ans, *stack, sep="")
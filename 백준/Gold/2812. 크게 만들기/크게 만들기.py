import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
s = deque(input().rstrip())
stack = []

for i in s: #1 9 2 4
    while stack and stack[-1] < i and k > 0:
        stack.pop()
        k -= 1

    stack.append(i)

if k > 0:
    stack = stack[:-k]

#print(k)
print(*stack, sep="")
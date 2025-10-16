import sys, math
import heapq
from collections import deque, defaultdict
input = sys.stdin.readline

s = input().rstrip()
m = int(input())

s1 = deque(s)
s2 = deque()
for i in range(m):
    cmd = input().split()
    if cmd[0] == "P":
        s1.append(cmd[1])
    elif cmd[0] == "L":
        if s1:
            s2.appendleft(s1.pop())
    elif cmd[0] == "D":
        if s2:
            s1.append(s2.popleft())
    else:
        if s1:
            s1.pop()

print(*s1, *s2, sep="")
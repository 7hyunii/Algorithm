import sys
input=sys.stdin.readline
from collections import deque
s = input().rstrip()
n = int(input())
d1 = deque()
d2 = deque()

for i in s:
    d1.append(i)

for _ in range(n):
    a = input().split()
    if a[0]=='L':
        if d1:
            d2.appendleft(d1.pop())
    if a[0]=='D':
        if d2:
            d1.append(d2.popleft())
    if a[0]=='B':
        if d1:
            d1.pop()     
    if a[0]=='P':
        d1.append(a[1])

print(*d1, *d2, sep="")
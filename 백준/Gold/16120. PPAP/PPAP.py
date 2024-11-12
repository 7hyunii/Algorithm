import sys
input=sys.stdin.readline
from collections import deque

n = input().rstrip()
d = []
for i in n:
    d.append(i)
    if d[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(4):
            d.pop()
        d.append('P')

if d == ['P', 'P', 'A', 'P'] or d == ['P']:
    print("PPAP")
else:
    print("NP")
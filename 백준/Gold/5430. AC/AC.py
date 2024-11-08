import sys
input=sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    S = input().rstrip()[1:-1]
    arr = deque(S.split(','))
    Toggle = 0
    printed = 0

    if n == 0:
        arr = deque()

    for i in range(len(p)):
        if p[i] == 'R':
            Toggle += 1
        if p[i] == 'D':
            if len(arr) == 0:
                print("error")
                Toggle = 0
                printed = 1
                break
            if Toggle % 2 == 0:
                arr.popleft()
            else:
                arr.pop()

    if printed:
        continue
    if Toggle % 2:
        arr.reverse()
        print(f"[{','.join(arr)}]")
    else:
        print(f"[{','.join(arr)}]")
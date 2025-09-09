from collections import deque
import sys
input = sys.stdin.readline
x = input()
while x[0] != '.':
    d = deque()
    for i in x:
        if i == '(' or i == ')' or i == '[' or i == ']':
            d.append(i)

    for _ in range(100):
        new_d = deque()
        i = 0
        while i < len(d):
            if i < len(d) - 1 and ((d[i] == '(' and d[i + 1] == ')') or (d[i] == '[' and d[i + 1] == ']')):
                i += 2
            else:
                new_d.append(d[i])
                i += 1
        if len(new_d) == len(d):
            break
        else:
            d = new_d

    if len(d) != 0:
        print("no")
    else:
        print("yes")
    x = input()
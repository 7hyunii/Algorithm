import sys, math
import heapq
from collections import deque, defaultdict
input = sys.stdin.readline

Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, input().split())

def cal(t):
    fx = Ax*t + Bx* (1 - t)
    fy = Ay*t + By* (1 - t)
    sx = Cx*t + Dx* (1 - t)
    sy = Cy*t + Dy* (1 - t)
    return ((fx-sx) ** 2 + (fy-sy) ** 2) ** 0.5

left, right = 0, 1
for _ in range(500):
    m1 = left + (right-left) / 3
    m2 = right - (right-left) / 3

    if cal(m1) > cal(m2):
        left = m1
    else:
        right = m2

print(cal(left))
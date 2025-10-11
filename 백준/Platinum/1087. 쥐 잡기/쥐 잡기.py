import sys, math
import heapq
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
mouse = []
for _ in range(n):
    mouse.append(list(map(int, input().split())))

def cal(t):
    pos = []
    for px, py, vx, vy in mouse:
        pos.append([px + vx*t, py + vy*t])
    # max_x
    X = sorted(pos)
    L = X[-1][0]-X[0][0]
    # max_y
    Y = sorted(pos, key=lambda x:x[1])
    L = max(L, Y[-1][1]-Y[0][1])

    return L

left, right = 0, 10000
for _ in range(500):
    m1 = left + (right-left) / 3
    m2 = right - (right-left) / 3

    if cal(m1) > cal(m2):
        left = m1
    else:
        right = m2

print(cal(left))

"""
t를 삼분탐색
=> x, y 좌표 중 큰 값이 L

"""
import sys, math
import heapq
from collections import deque, defaultdict
input = sys.stdin.readline
import typing

while True:
    n, m = input().split()
    n: int = int(n)
    m: int = int(round(float(m) * 100))
    if n == 0 and m == 0:
        break

    arr: typing.List[typing.Tuple[int, int]] = []
    for _ in range(n):
        c, p = input().split()
        c: int = int(c)
        p: int = int(round(float(p) * 100))
        arr.append((c, p))
    #print(arr)

    dp: typing.List[int] = [0] * (m+1)
    for cal, price in arr:
        for x in range(price, m+1):
            dp[x] = max(dp[x], dp[x-price] + cal)
        #print(dp)

    print(dp[m])


"""
m: 총 금액
c: 가격
p: 칼로리

dp[x] : x원일 때 얻을 수 있는 최대 칼로리
    사탕 별로 돌면서 dp 갱신 
    700 ->  ~~ 700
    199 ->  dp[200] = max(0, 199) = 199
            dp[400] = max(0, 199 + 199) = 398
            dp[600] = max(0, 398 + 199) = 597
            dp[800] = max(700, 597 + 199) = 796


"""

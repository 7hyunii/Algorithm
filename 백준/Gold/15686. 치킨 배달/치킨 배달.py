import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
Home = []
Chicken = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1:
            Home.append((i+1, j+1))
        if arr[j] == 2:
            Chicken.append((i+1, j+1))

P = combinations(Chicken, m)
ans = float('inf')
for comb in P: 
    cur = 0
    for hx, hy in Home:
        dist = float('inf')
        for cx, cy in comb:
            d = abs(cx - hx) + abs(cy - hy)
            dist = min(dist, d)
        cur += dist
    ans = min(ans, cur)

print(ans)
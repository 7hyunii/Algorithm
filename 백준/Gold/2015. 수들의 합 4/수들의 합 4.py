import sys
input = sys.stdin.readline

from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))

pf = defaultdict(int)
pf[0] = 1
cur = 0
ans = 0
for i in arr:
    cur += i

    ans += pf[cur - k]
    pf[cur] += 1
    #print(pf)

print(ans)
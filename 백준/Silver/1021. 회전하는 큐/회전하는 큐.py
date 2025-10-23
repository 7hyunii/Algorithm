import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
arr = list(map(int, input().split()))
dq = deque(range(1, n+1))
ans = 0
for i in arr:
    idx = dq.index(i)
    ans += min(idx, len(dq) - idx)

    dq.rotate(-idx)
    dq.popleft()

print(ans)
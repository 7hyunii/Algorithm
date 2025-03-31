import sys
input = sys.stdin.readline
import bisect

n, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
Light = list(map(int, input().split()))

OFF, TogOFF = 0, 0
ans = 0
for i in range(n):
    if Light[i] == 0:
        OFF += 1
    else:
        idx = bisect.bisect_left(A, OFF)
        if idx < len(A) and A[idx] <= TogOFF + OFF:
            TogOFF += 1
        else:
            ans += 1

print(ans)
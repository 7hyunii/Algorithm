import sys
input = sys.stdin.readline
from collections import deque

n, d = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()
dp = [0] * n
for i in range(n):

    while q and q[0][1] < i-d:      # over D
        q.popleft()
    
    if q and q[0][0] > 0:
        dp[i] = q[0][0] + arr[i]
    else:
        dp[i] = arr[i]

    while q and q[-1][0] <= dp[i]:
        q.pop()

    q.append((dp[i], i))
    # print(q)

print(max(dp))

"""
10 2
2 7 -5 -4 10 -5 -5 -5 30 -10

2 9  4  5 15 10 10  5 40  30

i   Q       push    popleft pop
0   2       2
1   9       9               2
2   9 4     4                      
3   9 5     5               4
4   15      15      9       5
5   15 10   10      
6   15 10   10              10
7   10 5    5       15
8   40      40              5 10
9   40 30   30  


"""
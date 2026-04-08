import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

q = deque()
q.append((0, 0))
for i in range(1, n+1):
    while q and q[0][1] < i-k-1:      # over k
        q.popleft()  

    check = q[0][0] + arr[i-1]

    while q and q[-1][0] >= check:
        q.pop()

    q.append((check, i))
    # print(q)

while q and q[0][1] < n-k:
    q.popleft()

print(sum(arr) - q[0][0])

"""
제외할 소에 포인트!

k = 2
50 10 40 30 100

arr     q               popleft pop
0       0
50      0 50            
10      0 10                    50
40      0 10 40         
30      10 40           0       40                  
100     10 40 110
        40 110

"""
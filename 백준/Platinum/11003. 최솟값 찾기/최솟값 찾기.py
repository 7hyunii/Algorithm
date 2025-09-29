import sys
input=sys.stdin.readline
from collections import deque
N,L=map(int, input().split())
a=list(map(int, input().split()))   
d=deque()
#Monotone Queue
for i in range(N):
    while d and d[-1][1]>a[i]:
        d.pop()
    d.append((i, a[i]))
    #print(d)

    if d[0][0]<=i-L:
        d.popleft()
    print(d[0][1], end=" ")

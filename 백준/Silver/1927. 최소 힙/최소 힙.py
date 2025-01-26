import sys
input=sys.stdin.readline
from queue import PriorityQueue
n=int(input())
Q=PriorityQueue()
for i in range(n):
    m=int(input())
    if m==0 and Q.empty():
        print(0)
    elif m==0:
        print(Q.get())
    else:
        Q.put(m)
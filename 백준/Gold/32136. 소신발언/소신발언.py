#삼분탐색 연습
import sys, math
import heapq
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def cal(idx):
    maxTime = 0
    for j in range(n):
        time = abs(idx - (j+1)) * arr[j]
        maxTime = max(time, maxTime)
    return maxTime

left, right = 1, n 
while right - left >= 3:
    m1 = left + (right-left) // 3
    m2 = right - (right-left) // 3

    t1 = cal(m1)
    t2 = cal(m2)
    
    if t1 > t2:
        left = m1
    else:
        right = m2

ans = float('inf')
for i in range(left, right+1):
    ans = min(ans, cal(i))

print(ans)
 
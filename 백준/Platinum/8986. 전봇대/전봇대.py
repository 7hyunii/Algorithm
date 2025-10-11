import sys, math
import heapq
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def cal(x): # 함수
    total = 0
    for i in range(n):
        total += abs(arr[i] - x*i)
    return total

left, right = 1, 1000000001
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

import sys
input = sys.stdin.readline

n, T = map(int, input().split())
arr = []
for _ in range(n):
    L, R = map(int, input().split())
    arr.append((L, R))

minTotal = sum(L for L, _ in arr)
maxTotal = sum(R for _, R in arr)
if minTotal > T or maxTotal < T:
    print(-1)
    quit()

S = float('inf')
left, right = 0, max(R for _, R in arr)
while left <= right:
    mid = (left + right) // 2
    Tog = 0
    maxSum = 0

    for L, R in arr:
        if L > mid:
            Tog = 1
            break
        maxSum += min(R, mid)
    
    #print(mid, maxSum)
    if not Tog and T <= maxSum:
        S = min(S, mid)
        right = mid - 1
    else:
        left = mid + 1

print(S)
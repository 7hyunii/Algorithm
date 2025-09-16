import sys
input = sys.stdin.readline

n, m, L = map(int, input().split())
if n == 0:
    arr = [0, L]
else:
    arr = [0] + list(map(int, input().split())) + [L]
    arr.sort()

dist = []
for i in range(1, len(arr)):
    dist.append(arr[i] - arr[i-1])

left = 1
right = max(dist)
ans = max(dist)
while left <= right:
    mid = (left + right) // 2

    add = 0
    for check in dist:
        if check > mid:
            add += (check - 1) // mid
    
    if add <= m:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)

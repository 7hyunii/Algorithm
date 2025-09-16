import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = max(arr) - min(arr)
ans = max(arr) - min(arr)
while left <= right:
    mid = (left + right) // 2

    cnt = 1
    group = []
    for i in range(n):
        group.append(arr[i])
        if max(group) - min(group) > mid:
            group = [arr[i]]
            cnt += 1

    if cnt <= m:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
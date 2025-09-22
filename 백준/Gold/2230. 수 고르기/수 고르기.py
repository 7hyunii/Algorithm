import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

left, right = 0, 0
ans = float('inf')
while right < n:
    mid = arr[right] - arr[left]

    if mid >= m:
        ans = min(ans, mid)
        left += 1
        if left > right:
            break

    else:
        right += 1

print(ans)
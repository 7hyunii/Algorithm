import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())

ans = 0
left, right = 0, n-1
while left < right:
    s = arr[left] + arr[right]
    if s == x:
        ans += 1
        left += 1
        right -= 1
    elif s < x:
        left += 1
    else:
        right -= 1

print(ans)
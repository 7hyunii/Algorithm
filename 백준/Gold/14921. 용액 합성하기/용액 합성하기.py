import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = float('inf')
left = 0
right = n-1
while left < right:
    check = arr[left] + arr[right]

    if check == 0:
        print(0)
        quit()

    if abs(check - 0) < abs(ans - 0):
        ans = check

    if check - 0 < 0:
        left += 1
    else:
        right -= 1

print(ans)

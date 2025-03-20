import sys
input = sys.stdin.readline
ffff = float('inf')

n, S = map(int, input().split())
arr = list(map(int, input().split()))

#print(arr)
left, right = 0, 0
Sum = 0
ans = ffff
while right < n:
    Sum += arr[right]
    right += 1

    while Sum >= S:
        ans = min(ans, right-left)
        Sum -= arr[left]
        left += 1

if ans == ffff:
    print(0)
else:
    print(ans)
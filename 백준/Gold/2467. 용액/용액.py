import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
left, right = 0, n-1
Q1, Q2 = 0, 0
Prior = float('inf')

while left < right:
    Now = arr[left] + arr[right]

    if abs(Now) < abs(Prior):
        Q1, Q2, Prior = arr[left], arr[right], Now

    if Now > 0:
        right -= 1
    elif Now < 0:
        left += 1
    else:
        break

print(Q1, Q2)
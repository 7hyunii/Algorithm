import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == x:
            ans += 1
        if arr[i] + arr[j] > x:
            break

print(ans)
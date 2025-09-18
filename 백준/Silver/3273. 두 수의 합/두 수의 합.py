import sys
input = sys.stdin.readline

n = int(input())
arr = set(map(int, input().split()))
x = int(input())

ans = 0
for i in arr:
    if x - i in arr:
        ans += 1

print(ans//2)
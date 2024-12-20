import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+5)
stair = [0] * (n+5)
for i in range(n):
    stair[i] = int(input())

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
for i in range(2, n+1):
    dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

print(dp[n-1])
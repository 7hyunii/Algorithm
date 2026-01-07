import sys
input = sys.stdin.readline
mod = 1000000000
########################################
n = int(input())
dp = [[0]*10 for _ in range(n+1)]

for i in range(1,10):
    dp[1][i] = 1

for i in range(2, n+1):
    dp[i][0] = dp[i-1][1] % mod
    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod
    dp[i][9] = dp[i-1][8] % mod

ans = 0
for i in range(10):
    ans += dp[n][i]
    ans %= mod

print(ans)

"""
1 : 1,2,3,4,5,6,7,8,9
2 : 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98

"""
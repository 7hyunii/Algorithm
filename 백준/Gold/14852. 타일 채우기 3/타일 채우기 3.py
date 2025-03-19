import sys
input = sys.stdin.readline

dp = [0, 2, 7, 22]
psum = 0
n = int(input())
for i in range(4, n+1):
    psum += dp[-3]
    dp.append((dp[i-1]*2 + dp[i-2]*3 + psum*2 + 2) % 1000000007)

print(dp[n])
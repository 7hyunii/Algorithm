import sys
input=sys.stdin.readline
str1=input()
str2=input()

m=len(str1)
n=len(str2)
dp=[[0]*(n) for _ in range(m)]

for i in range(1, m):
    for j in range(1, n):
        if str1[i-1]==str2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

#print(*dp)
print(dp[m-1][n-1])
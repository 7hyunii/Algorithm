import sys
input=sys.stdin.readline
A=int(input())
if A==1:
    print(1)
elif A==2:
    print(3)
else:
    dp=[0]*(A+1)
    dp[1]=1
    dp[2]=3
    for i in range(3, A+1):
        dp[i]=(dp[i-1]+2*dp[i-2])%10007
    print(dp[A])
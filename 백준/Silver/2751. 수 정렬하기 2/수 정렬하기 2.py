import sys
input=sys.stdin.readline
A=int(input())
dp=[]
for i in range(A):
    N=int(input())
    dp.append(N)

print(*sorted(dp), sep="\n")
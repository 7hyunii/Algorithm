import sys
input=sys.stdin.readline
n, s=map(int, input().split())
d=list(map(int, input().split()))
count=0
for i in range(1, 2**n):
    sum=0
    for j in range(n):
        if i&(1<<j):
            sum+=d[j]
    if sum==s:
        count+=1

print(count)
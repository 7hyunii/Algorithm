import sys
input=sys.stdin.readline
from collections import deque
n=list(input().strip())
m=n[::-1]
d=deque()
for i in n:
    d.appendleft(i)
    
ans=len(n)
if n==m:
    print(len(n))
else:
    for i in range(len(n)):
        count=0
        d.appendleft(0)
        for j in range(i+1, len(n)):
            if n[j]==d[j]:
                count+=1
            else:
                break
        ans+=1
        if count==len(n)-i-1:
            break
    print(ans)
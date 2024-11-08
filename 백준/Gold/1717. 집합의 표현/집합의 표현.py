import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
n, m=map(int, input().split())
parent=[i for i in range(n+1)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(x, y):
    x=find(x)
    y=find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

for _ in range(m):
    k, a, b=map(int, input().split())
    if k==0:
        union(a, b)
    else:
        if find(a)==find(b):
            print("YES")
        else:
            print("NO")
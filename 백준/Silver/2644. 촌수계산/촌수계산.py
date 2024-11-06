import sys
input=sys.stdin.readline
from collections import defaultdict

Graph = defaultdict(list)
visited = []
count = 0
def DFS(start, end, depth):
    if start == end:
        print(depth)
        quit()
    visited.append(start)
    for i in Graph[start]:
        if i not in visited:
            DFS(i, end, depth+1)


n = int(input())
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    Graph[x].append(y)
    Graph[y].append(x)

count = 0
DFS(a, b, 0)
print(-1)
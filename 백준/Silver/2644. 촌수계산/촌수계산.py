import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
graph = defaultdict(list)
s, e = map(int, input().split())
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()
ans = 0
def dfs(cur, depth):
    if cur == e:
        print(depth)
        sys.exit()

    for nxt in graph[cur]:
        if nxt not in visited:
            visited.add(nxt)
            dfs(nxt, depth+1)

visited.add(s)
dfs(s, 0)
print(-1)
import sys
input = sys.stdin.readline
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)

def DFS(start):
    visited.add(start)

    if not Graph[start]:
        print("yes")
        quit()

    if 0 not in Graph[start]:
        for node in Graph[start]:
            if node not in visited:
                DFS(node)



Graph = defaultdict(list)
n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    Graph[a].append(b)
S = int(input())
s = list(map(int, input().split()))
for i in range(S):
    Graph[s[i]].append(0)

#print(Graph)
visited = set()
DFS(1)

print("Yes")
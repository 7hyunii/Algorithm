import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**7)

def DFS(K):
    global ans
    if not Graph[K]:
        ans += 1
        return

    for node in Graph[K]:
        DFS(node)

Graph = defaultdict(list)
N = int(input())
info = list(map(int, input().split()))
delete = int(input())
root = -1
for i in range(N):
    if info[i] == -1:
        root = i
        continue
    if i == delete:    #그냥 끊어버리자
        continue
    Graph[info[i]].append(i)

ans = 0
if root == delete:
    print(0)
else:
    DFS(root)
    print(ans)
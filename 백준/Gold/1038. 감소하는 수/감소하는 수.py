import sys
input = sys.stdin.readline

n = int(input())

if n <= 9:
    print(n)
    quit()

#9876543210가 최대
visited = []
def DFS(n, last):
    visited.append(n)
    for i in range(0, last):
        DFS(n*10 + i, i)

for i in range(10):
    DFS(i, i)

visited.sort()

if n >= len(visited):
    print(-1)
else:
    print(visited[n])
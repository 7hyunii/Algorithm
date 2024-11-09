from collections import deque
import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
n, m, v = map(int, input().split())
List = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    List[a].append(b)
    List[b].append(a)

for i in range(1, n+1):
    List[i].sort()

def BFS(index):
    d = deque()
    d.append(index)
    c = 1
    Visit[index] = 1
    while d:
        gone = d.popleft()
        for i in List[gone]:
            if not Visit[i]:
                c += 1
                Visit[i] = c
                d.append(i)
            
Visit = [0] * (n+1)
BFS(v)
for i in range(1, n+1):
    print(Visit[i])
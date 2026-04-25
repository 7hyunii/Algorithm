from collections import deque
import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
n, m, v = map(int, input().split())
List=[[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    List[a].append(b)
    List[b].append(a)

for i in range(1, n+1):
    List[i].sort()

#DFS는 주로 재귀로 구현
def DFS(index): 
    print(index, end=" ")
    Visit[index] = 1
    for i in List[index]:
        if not Visit[i]:
            DFS(i)

#BFS는 큐로 구현
def BFS(index):
    d = deque()
    d.append(index)
    Visit[index] = 1
    while d:
        gone = d.popleft()
        print(gone, end=" ")
        for i in List[gone]:
            if not Visit[i]:
                Visit[i] = 1
                d.append(i)
            
Visit = [0] * (n+1)
DFS(v)
print()
Visit = [0] * (n+1)
BFS(v)
import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def BFS(start, end):
    Q = deque()
    Q.append(start)
    visited[start] = 0
    while Q:
        current = Q.popleft()
        if current == end:
            print(visited[current])
            quit()
        
        for next in [current-1, current+1, current*2]:
            if 0 <= next <= 100000 and visited[next] == -1:
                visited[next] = visited[current] + 1
                Q.append(next)

n, m = map(int, input().split())
visited = defaultdict(lambda:-1)
BFS(n, m)
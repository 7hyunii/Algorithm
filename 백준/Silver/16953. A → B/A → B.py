import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def BFS(n, m):
    visited = set()
    Q = deque()
    Q.append((n, 1))

    while Q:
        v, Cnt = Q.popleft()

        if v == m:
            print(Cnt)
            quit()

        if v < m:
            if v*2 not in visited:
                Q.append((v*2, Cnt + 1))
                visited.add(v*2)
            if int(str(v) + "1") not in visited:
                Q.append((int(str(v) + "1"), Cnt + 1))
                visited.add(int(str(v) + "1"))
            
    print(-1)


Graph = defaultdict(list)
n, m = map(int, input().split())

BFS(n, m)
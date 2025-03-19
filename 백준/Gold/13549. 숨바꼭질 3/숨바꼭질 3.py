import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def BFS(n, m):
    visited = set()
    Q = deque()
    Q.append((n, 0))

    while Q:
        v, Cnt = Q.popleft()

        if v == m:
            print(Cnt)
            return

        if 0 <= v*2 <= 100000 and v*2 not in visited:
            Q.append((v*2, Cnt))
            visited.add(v*2)
        if 0 <= v-1 <= 100000 and v-1 not in visited:
            Q.append((v-1, Cnt+1))
            visited.add(v-1)
        if 0 <= v+1 <= 100000 and v+1 not in visited:
            Q.append((v+1, Cnt+1))
            visited.add(v+1)

    print(n)


Graph = defaultdict(list)
n, m = map(int, input().split())

BFS(n, m)
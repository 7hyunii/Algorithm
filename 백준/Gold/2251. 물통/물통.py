import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def BFS(a, b, c):
    visited.add((0, 0, c))

    Q = deque()
    Q.append((0, 0, c))

    while Q:
        a, b, c = Q.popleft()

        for x, y, z in Check(a, b, c):
            if (x, y, z) not in visited:
                visited.add((x, y, z))
                Q.append((x, y, z))
                if x == 0:
                    ans.add(z)
        

def Check(a, b, c):
    check = []
    if c+a > A:
        check.append((A, b, (c+a)-A))
    else:
        check.append((c+a, b, 0))
    if c+b > B:
        check.append((a, B, (c+b)-B))
    else:
        check.append((a, c+b, 0))
    if a+b > B:
        check.append(((a+b)-B, B, c))
    else:
        check.append((0, a+b, c))
    check.append((0, b, a+c))
    if b+a > A:
        check.append((A, (a+b)-A, c))
    else:
        check.append((b+a, 0, c))
    check.append((a, 0, b+c))

    return check

A, B, C = map(int, input().split())
visited = set()
ans = set()
ans.add(C)

BFS(0, 0, C)
ans = sorted(ans)
print(*ans)
import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
cnt = 0
Min = float('inf')
visited = [-1] * 100001
Q = deque()

visited[n] = 0
Q.append((n, 0))
while Q:
    v, time = Q.popleft()

    if time > Min:
        break

    if v == k:
        if Min > time:
            Min = time
            print(Min)
        if Min == time:
            cnt += 1
        continue

    for nxt in (v - 1, v + 1, v * 2):
        if 0 <= nxt <= 100000:
            if visited[nxt] == -1 or visited[nxt] == time + 1:
                visited[nxt] = time + 1
                Q.append((nxt, time + 1))

print(cnt)
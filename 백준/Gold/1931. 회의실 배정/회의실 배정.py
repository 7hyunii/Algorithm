import sys, heapq
input = sys.stdin.readline

heap = []   
n = int(input())
for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(heap, (e, s))

ans = 1
e, s = heapq.heappop(heap)
while heap:
    E, S = heapq.heappop(heap)
    if S >= e:
        ans += 1
        e = E

print(ans)
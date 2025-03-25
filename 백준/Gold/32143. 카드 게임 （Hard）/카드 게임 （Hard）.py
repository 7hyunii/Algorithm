import sys
input = sys.stdin.readline
import heapq

H = int(input())
N, Q = map(int, input().split())
InitN = list(map(int, input().split()))
Card = []
total = 0
for i in InitN:
    heapq.heappush(Card, i)
    total += i

for i in range(Q+1):
    if i > 0:
        a = int(input())
        total += a
        heapq.heappush(Card, a)

    if total < H:
        print(-1)

    else:
        while Card and total - Card[0] >= H:
            total -= heapq.heappop(Card)
        #print(Card)
        print(len(Card))
import sys
input = sys.stdin.readline
from collections import deque

q = int(input())
arr = deque()

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]
        arr.append(x)

    if query[0] == 2:
        n = len(arr)
        mid = n // 2

        arr_list = list(arr)
        p1 = arr_list[:mid]
        p2 = arr_list[mid:]
        s1 = sum(p1)
        s2 = sum(p2)

        if s1 > s2:
            print(s2)
            arr = deque(p1)
        else:
            print(s1)
            arr = deque(p2) 

print(*arr)
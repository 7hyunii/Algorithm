import sys
input = sys.stdin.readline

q = int(input())
arr = []

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]
        arr.append(x)

    if query[0] == 2:
        n = len(arr)
        mid = n // 2
        
        s1 = sum(arr[:mid])
        s2 = sum(arr[mid:])

        if s1 > s2:
            print(s2)
            arr = arr[:mid]
        else:
            print(s1)
            arr = arr[mid:]

print(*arr)
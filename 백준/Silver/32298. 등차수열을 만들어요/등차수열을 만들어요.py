import sys
input = sys.stdin.readline
import math

n, m = map(int, input().split())

check = [True] * 20000001
check[0] = check[1] = False
for i in range(2, int(math.sqrt(2000000)) + 1):
    if check[i]:
        for j in range(i * i, 2000001, i):
            check[j] = False

Tog = True
for i in range(1, 2000001):
    arr = [i + j * m for j in range(n)]

    if all(not check[num] for num in arr):  
        print(*arr)  # 찾으면 즉시 출력
        quit()

print(-1)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, list(input().strip()))) for _ in range(N)]
B = [list(map(int, list(input().strip()))) for _ in range(N)]

def flip(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            flip(i, j)
            cnt += 1

is_same = True
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            is_same = False
            break
    if not is_same:
        break

if is_same:
    print(cnt)
else:
    print(-1)

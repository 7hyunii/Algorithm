import sys
input = sys.stdin.readline

n = int(input())
count = 0
Board = [0] * (n + 1)
cols = [False] * (n + 1)          # 열 사용 여부 체크 (1 ~ n)
diag1 = [False] * (2 * n + 1)     # ↘ 대각선 (row + col)
diag2 = [False] * (2 * n + 1)     # ↙ 대각선 (row - col + n)

def queens(i):
    global count
    if i == n:
        count += 1
        
    for j in range(1, n + 1):  # 열 1~n 시도
        if not cols[j] and not diag1[i + 1 + j] and not diag2[i + 1 - j + n]:   #열, 오른쪽 아래 대각선, 왼쪽 아래 대각선
            Board[i + 1] = j
            cols[j] = diag1[i + 1 + j] = diag2[i + 1 - j + n] = True
            queens(i + 1)
            cols[j] = diag1[i + 1 + j] = diag2[i + 1 - j + n] = False  # 백트래킹

queens(0)
print(count)
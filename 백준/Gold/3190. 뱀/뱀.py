#
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
Board = [[0] * n for _ in range(n)] # 0: 빈칸

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    Board[x-1][y-1] = 1             # 1: 사과

L = int(input())

Dir = dict()
for _ in range(L):
    x, c = input().split()          
    Dir[int(x)] = c                 # 회전 해야 하는 시간 저장

################################### 입력 

dx = [1, 0, -1, 0]                  
dy = [0, 1, 0, -1]                  # (x, y)가 시계방향 회전 되게 (우 하 좌 상)
x, y = 0, 0
Snake = deque()                     # 앞 : 꼬리 // 뒤 : 머리
Snake.append((0, 0))                # 초기 뱀 위치
Turn = 0                            # 초기 방향 오른쪽 (1, 0) 
Time = 0

while 1:
    Time += 1
    nx = x + dx[Turn]
    ny = y + dy[Turn]

    if 0 <= ny < n and 0 <= nx < n and (ny, nx) not in Snake:
        if Board[ny][nx] == 1:      # 사과 있을 때              
            Board[ny][nx] = 0       # 사과 없애기
            Snake.append((ny, nx))  # 몸길이 추가 (머리에)
        else:                       # 사과 없을 때
            Snake.append((ny, nx))  # 몸길이 추가 (머리에)
            Snake.popleft()         # 꼬리 제거

        x, y = nx, ny

    else:
        print(Time)
        quit()

    if Time in Dir:                 # 방향 계산
        if Dir[Time] == "L":
            Turn = (Turn - 1) % 4   # 시계 방향으로 dx, dy를 만들었으므로 L방향은 -1 후 %4
        else:
            Turn = (Turn + 1) % 4   # ""                                  R방향은 +1 후 %4
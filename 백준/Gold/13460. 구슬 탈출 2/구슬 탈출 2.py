import sys
input = sys.stdin.readline
dydx = [(-1,0), (1,0), (0,-1), (0,1)]   # U, D, L, R
########################################
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input().strip()))
#print(board)

ans = 11
def dfs(depth, rx, ry, bx, by):
    global ans
    if depth >= ans or depth == 10:
        return
    
    for i in range(4):
        nrx, nry, r_result, nbx, nby, b_result = tilt(rx, ry, bx, by, dydx[i])

        if b_result:
            continue
        elif r_result:
            ans = min(ans, depth+1)
        else:
            dfs(depth+1, nrx, nry, nbx, nby)

def roll(x, y, dx, dy):
    while board[x+dx][y+dy] != "#" and board[x][y] != 'O':
        x += dx
        y += dy
        if board[x][y] == 'O':
            break
    return x, y, (board[x][y] == 'O')


def tilt(rx, ry, bx, by, dir):
    dy, dx = dir[0], dir[1]
    flag = "BLUE"                         # 우선순위 체크

    if dx == -1:
        if rx < bx:
            flag = "RED"
    if dx == 1:
        if rx > bx:
            flag = "RED"
    if dy == -1:
        if ry < by:
            flag = "RED"
    if dy == 1:
        if ry > by:
            flag = "RED"

    if flag == "RED":
        rx, ry, red_hole = roll(rx, ry, dx, dy)
        bx, by, blue_hole = roll(bx, by, dx, dy)
    else:
        bx, by, blue_hole = roll(bx, by, dx, dy)
        rx, ry, red_hole = roll(rx, ry, dx, dy)

    if not red_hole and not blue_hole and rx == bx and ry == by:
        if flag == "RED":
            bx -= dx
            by -= dy
        else:
            rx -= dx
            ry -= dy

    return rx, ry, red_hole, bx, by, blue_hole


for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j
dfs(0, rx, ry, bx, by)
print(ans if ans <= 10 else -1)


"""
RED : R
BLUE : B
Hole : O
WALL : #


"""
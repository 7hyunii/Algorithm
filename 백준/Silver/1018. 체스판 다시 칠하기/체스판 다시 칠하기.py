import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Board = [input().strip() for _ in range(N)]

ans = []
for i in range(N - 7):
    for j in range(M - 7):
        cnt1, cnt2 = 0, 0
        check = [row[j:j+8] for row in Board[i:i+8]]
        for a in range(8):
            for b in range(8):
                if (a+b) % 2:
                    if check[a][b] != 'W':
                        cnt1 += 1
                    if check[a][b] != 'B':
                        cnt2 += 1
                else:
                    if check[a][b] != 'B':
                        cnt1 += 1
                    if check[a][b] != 'W':
                        cnt2 += 1
        ans.append(min(cnt1, cnt2))

print(min(ans))
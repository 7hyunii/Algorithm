import sys
input = sys.stdin.readline

n, h = map(int, input().split())
arr = [int(input()) for _ in range(n)]
# 1 5 3 3 5 1
up = [0] * (h+1)    #종유석
down = [0] * (h+1)  #석순
for i in range(n):
    if i % 2:
        down[arr[i]] += 1
    else:
        up[h - arr[i] + 1] += 1

for i in range(h-1, 0, -1):
    down[i] = down[i] + down[i+1]

for i in range(1, h+1):
    up[i] = up[i] + up[i-1]

cnt = 0
min_value = n+1
for i in range(1, h+1):
    if up[i] + down[i] < min_value:
        min_value = up[i] + down[i]
        cnt =1
    elif up[i] + down[i] == min_value:
        cnt += 1

print(min_value, cnt)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
score = list(map(int, input().split()))

left = 0                #min
right = sum(score)      #max
ans = 0
while left <= right:
    mid = (left + right) // 2

    cnt = 0
    group = 0
    for i in range(n):               #가능한지 확인
        group += score[i]
        if group >= mid:
            cnt += 1
            group = 0
    
    if cnt >= k:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)

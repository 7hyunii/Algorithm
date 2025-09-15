import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

left = 1                        #min
right = house[-1] - house[0]    #max
ans = 0
while left <= right:
    mid = (left + right) // 2

    cnt = 1
    prior = house[0]
    for i in range(1, n):               #가능한지 확인
        if house[i] - prior >= mid:
            prior = house[i]
            cnt += 1
    
    if cnt >= c:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)

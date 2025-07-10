import sys
input=sys.stdin.readline

#sleep = b * x(0 ~ a-1)
#after sleep -> A : a-x
n, a, b = map(int, input().split())
T = list(map(int, input().split()))
T.sort()

ans_max = 0
for x in range(a):
    sleep = b*x     #sleep time
    for i in range(n):  #i : 잠 자는 시기 결정
        total = 0
        used = [False] * n
        cnt = 0

        #잠자기 전
        for j in range(n):
            if cnt == i:
                break
            if total + a <= T[j] and not used[j]:
                total += a
                cnt += 1
                used[j] = True
        #잠        
        total += sleep

        #잠잔 후
        for j in range(n):
            if total + (a-x) <= T[j] and not used[j]:
                total += a-x
                cnt += 1    
                used[j] = True    
        ##
        if cnt == n:
            print(cnt)
            quit()

        ans_max = max(cnt, ans_max)

print(ans_max)
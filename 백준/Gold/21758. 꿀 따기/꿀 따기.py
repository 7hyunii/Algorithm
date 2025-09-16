import sys
input = sys.stdin.readline

n = int(input())
honey = list(map(int, input().split()))
pf = [0] * (n+1)
for i in range(n):
    pf[i+1] = pf[i] + honey[i]

ans = 0
#Right
#bee1은 왼쪽 끝 고정
for bee2 in range(1, n-1):
    Check1 = pf[-1] - pf[1] - honey[bee2]
    Check2 = pf[-1] - pf[bee2+1]
    ans = max(ans, Check1 + Check2)

#Left
#bee1는 오른쪽 끝 고정
for bee2 in range(1, n-1):
    Check1 = pf[n-1] - honey[bee2]
    Check2 = pf[bee2]
    ans = max(ans, Check1 + Check2)

#Other?
#bee1, bee2가 양쪽 끝에서 가운데로
for mid in range(1, n-1):
    Check1 = pf[mid+1] - pf[1]
    Check2 = pf[-2] - pf[mid]
    ans = max(ans, Check1 + Check2)

print(ans)
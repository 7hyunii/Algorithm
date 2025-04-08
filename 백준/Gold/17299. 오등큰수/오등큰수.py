#오큰수에다가 Cnt만 추가 된거 아님?
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
Cnt = [0] * 1000001
ans = [-1] * n

for i in A:
    Cnt[i] += 1

Stack = []
for i in range(n):
    while Stack and Cnt[A[Stack[-1]]] < Cnt[A[i]]:  #오등큰수 조건
        #print(ans, Stack)
        ans[Stack.pop()] = A[i]
    Stack.append(i)

print(*ans)
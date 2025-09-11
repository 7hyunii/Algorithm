import sys
input = sys.stdin.readline

N, L = map(int, input().split())

for l in range(L, 101):
    #등차수열의 합 공식 응용
    n = N - (l-1) * l // 2

    if n % l == 0:
        a = n // l

        if a >= 0:
            for i in range(a, a+l):
                print(i, end=" ")
            quit()

print(-1)
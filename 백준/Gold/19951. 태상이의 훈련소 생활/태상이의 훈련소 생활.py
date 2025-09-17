import sys
input = sys.stdin.readline

n, m = map(int, input().split())
h = list(map(int, input().split()))

K = [0] * n
for _ in range(m):
    a, b, k = map(int, input().split())
    K[a-1] += k
    if b < n:
        K[b] -= k

for i in range(1, n):
    K[i] += K[i-1]

for i in range(n):
    print(h[i] + K[i], end=" ")
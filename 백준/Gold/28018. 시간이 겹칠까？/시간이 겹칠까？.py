import sys
input = sys.stdin.readline

n = int(input())

Time = [0] * 1000002
arr = [0 for _ in range(1000002)]

for _ in range(n):
    a, b = map(int, input().split())
    Time[a] += 1
    Time[b+1] -= 1

Q = int(input())

for i in range(1, 1000001):
    arr[i] = arr[i-1] + Time[i]

T = list(input().split())

for i in T:
    print(arr[int(i)])
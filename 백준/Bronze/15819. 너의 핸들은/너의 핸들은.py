import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr = []
for _ in range(a):
    s = input()
    arr.append(s)

arr.sort()
print(arr[b-1])
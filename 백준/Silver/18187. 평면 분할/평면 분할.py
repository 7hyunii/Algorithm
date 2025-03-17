import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (n+2)
arr[1], arr[2] = 2, 4

k = 3
for i in range(3, n+1):
    arr[i] = arr[i-1] + k
    if i % 3 != 0:
        k += 1

print(arr[n])
#print(arr)
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = [0] * n
for i in range(n):
    K = i+1
    left = arr[i]

    passed = 0
    for j in range(n):
        if ans[j] == 0 and left == passed:
            ans[j] = K
            break
        elif ans[j] == 0:
            passed += 1

print(*ans)
import sys
input = sys.stdin.readline
from itertools import combinations
from bisect import bisect_left, bisect_right
########################################
n, s = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
left, right = nums[:n//2], nums[n//2:]
leftSum, rightSum = [], []

def getSum(arr, sumArr):
    sumArr.append(0)    # 공집합 추가
    for i in range(1, len(arr)+1):
        for c in combinations(arr, i):
            sumArr.append(sum(c))
    sumArr.sort()

getSum(left, leftSum)
getSum(right, rightSum)
# print(leftSum)
# print(rightSum)

for i in leftSum:
    target = s - i
    ans += bisect_right(rightSum, target) - bisect_left(rightSum, target)   # count는 느릴듯

if s == 0:  # 빈집합 제외
    ans -= 1
print(ans)

"""
left / right

- case 0 check

"""
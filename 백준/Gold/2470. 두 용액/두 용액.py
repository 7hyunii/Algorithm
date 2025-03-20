import sys
input = sys.stdin.readline
ffff = float('inf')

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left, right = 0, n-1
valueCheck = ffff
Ans = (0, 0)

while left < right:
    curSum = arr[left] + arr[right]

    if curSum == 0:
        print(arr[left], arr[right])
        quit()
    
    if abs(curSum - 0) < abs(valueCheck- 0):
        valueCheck = curSum
        Ans = (arr[left], arr[right])

    if curSum > 0:
        right -= 1
    else:
        left += 1

print(Ans[0], Ans[1])
#print(valueCheck)
import sys
input = sys.stdin.readline

while 1:
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[1:] + [0]
    if n == 0:
        break

    stack = []
    ans = 0
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            h = arr[stack.pop()]
            if stack:
                w = i - stack[-1] - 1
            else:
                w = i
            ans = max(ans, h * w)
        stack.append(i)
    print(ans)


"""
2 1 4 5 1 3 3

"""
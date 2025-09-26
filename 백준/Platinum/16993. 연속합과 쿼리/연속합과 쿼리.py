import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tree = [(0, 0, 0, float('-inf'))] * (2*n)
for i in range(n):
    val = arr[i]
    tree[i+n] = (val, val, val, val)

def merge(left, right):
    if left[3] == float('-inf'):
        return right
    if right[3] == float('-inf'):
        return left
    
    S = left[2] + right[2]
    l = max(left[0], left[2] + right[0])
    r = max(right[1], right[2] + left[1])
    best = max(left[3], right[3], left[1] + right[0])

    return (l, r, S, best)

# 초기화
for i in range(n-1, 0, -1):
    tree[i] = merge(tree[i<<1], tree[i<<1|1])

def query(l, r):
    l = l - 1 + n
    r = r - 1 + n

    leftResult = (0, 0, 0, float('-inf'))
    rightResult = (0, 0, 0, float('-inf'))

    while l <= r:
        if l % 2:       # 오른쪽 자식
            leftResult = merge(leftResult, tree[l])
            l += 1

        if r % 2 == 0:  # 왼쪽 자식
            rightResult = merge(tree[r], rightResult)
            r -= 1
        
        l //= 2
        r //= 2

    return merge(leftResult, rightResult)


m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(query(a, b)[3])


"""
(left, right, sum, best)

[10, -4, 3]:
    l = (10, 10, 10, 10)

    [-4, 3]:
        l = max(-4, -1) = -1
        r = max(3, -1) = 3
        s = -4 + 3 = -1
        best = max(-4, 3, -1) = 3
    
    r = (-1, 3, -1, 3)

    =>  l = (10, 10-1) = 10
        r = (3, -1+10) = 9
        S = 10 -1 = 9
        best = (10, 3, 10-1) = 10
        =>  (10, 9, 9, 10)

"""
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = list(map(int, input().split())) + [0]
pf = [0]
for i in range(n):
    pf.append(arr[i] + pf[i])

stack = []
ans = 0
left, right = 1, 1
for i in range(n+1):
    while stack and arr[stack[-1]] > arr[i]:
        x = arr[stack.pop()]

        if stack:
            l = stack[-1]
        else:
            l = -1

        r = i
        if x * (pf[r] - pf[l+1]) > ans:
            ans = max(ans, x * (pf[r] - pf[l+1]))
            left = l+2
            right = r
    
    stack.append(i)

print(ans)
print(left, right)
        

"""
i~j prefix sum * min(i~j) = MAX_answer
               
3 1 6 4 5 2 0   0 3 4 10 14 19 21  

idxStack    stack   pop     l   r   prob
0           3       
1           1       3       0   1   9  
1 2         1 6     
1 3         1 4     6       1   3   36
1 3 4       1 4 5
1 3 5       1 4 2   5       3   5   25             
1 5         1 2     4       1   5   60


"""
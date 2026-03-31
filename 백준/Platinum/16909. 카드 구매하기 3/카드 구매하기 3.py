import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr1 = list(map(int, input().split()))

arr2 = arr1 + [0]
arr1 = arr1 + [float('inf')]

stackMax = []
stackMin = []
Max, Min = 0, 0 
for i in range(n+1):

    while stackMax and arr1[stackMax[-1]] < arr1[i]:
        x = stackMax.pop()

        if stackMax:
            L = x - stackMax[-1]
        else:
            L = x + 1

        R = i - x
        Max += arr1[x] * L * R

    stackMax.append(i)

    while stackMin and arr1[stackMin[-1]] > arr2[i]:
        x = stackMin.pop()

        if stackMin:
            L = x - stackMin[-1]
        else:
            L = x + 1

        R = i - x
        Min += arr2[x] * L * R

    stackMin.append(i)
    
print(Max-Min)
        

"""
ALL (max - min) = val

3
3 1
3 1 7
3 1 7 2
1
1 7
1 7 2
7
7 2
2

---

stack   pop max     idx L   R   val
3      
3, 1                
3, 7    1   7       2   2-1    1     
7       3   7       2   
7, 2
7, inf  2   inf     4
inf     7   inf     4
  

"""
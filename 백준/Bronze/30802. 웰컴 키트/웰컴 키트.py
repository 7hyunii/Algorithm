import sys
input=sys.stdin.readline
import itertools
n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
sum = 0
for i in size:
    if i % t:
        sum += i//t + 1
    else:
        sum += i//t

print(sum)
print(n//p, n%p)
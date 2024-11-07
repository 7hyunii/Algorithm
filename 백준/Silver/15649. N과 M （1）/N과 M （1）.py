import sys
input=sys.stdin.readline
import itertools
n, m = map(int, input().split())
arr = itertools.permutations(range(1, n+1), m)
for i in arr:
    print(*i)
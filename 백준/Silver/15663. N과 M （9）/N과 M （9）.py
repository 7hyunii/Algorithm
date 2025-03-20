import sys
input=sys.stdin.readline
import itertools
n, m = map(int, input().split())
a = list(map(int, input().split()))
arr = itertools.permutations(a, m)
arr = set(arr)
ans = sorted(arr)
for i in ans:
    print(*i)
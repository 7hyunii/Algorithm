import sys
input=sys.stdin.readline
import itertools
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
arr = itertools.combinations_with_replacement(a, m)
arr = set(arr)
ans = sorted(arr)
for i in ans:
    print(*i)
import sys
input=sys.stdin.readline
from collections import defaultdict
d = defaultdict(str)

n, m = map(int, input().split())
for _ in range(n):
	s = input().split()
	d[s[0]] = s[1]

for _ in range(m):
	s = input().rstrip()
	print(d[s])
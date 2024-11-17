import statistics
from collections import defaultdict
import sys
input=sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
print(int(round(statistics.fmean(a), 0)))
print(statistics.median(a))

d = defaultdict(int)
mode = 0
for i in a:
	d[i]+=1

srt = sorted(d.items(), key=lambda x: (-x[1], x[0]))
if len(srt) > 1 and srt[0][1] == srt[1][1]:
    mode = srt[1][0]
else:
    mode = srt[0][0]

print(mode)
print(max(a)-min(a))
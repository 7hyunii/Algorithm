import sys
input=sys.stdin.readline
from collections import deque
n = int(input())
for _ in range(n):
	s = input().rstrip()
	d1 = deque()
	d2 = deque()
	for i in s:
		if i == '<':
			if len(d1) != 0:
				d2.appendleft(d1.pop())
		elif i == '>':
			if len(d2) != 0:
				d1.append(d2.popleft())
		elif i == '-':
			if len(d1) != 0:
				d1.pop()
		else:
			d1.append(i)
			
	print(*d1, *d2, sep="")
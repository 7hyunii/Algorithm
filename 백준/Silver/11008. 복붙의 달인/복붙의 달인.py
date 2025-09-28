import sys
input = sys.stdin.readline

t = int(input())
for _  in range(t):
    s, p = input().rstrip().split()
    cnt = len(s) - s.count(p)*len(p) + s.count(p)
    print(cnt)
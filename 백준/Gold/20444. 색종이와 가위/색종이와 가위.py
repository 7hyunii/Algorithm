import sys
input = sys.stdin.readline

n, m = map(int, input().split())

start, end = 0, n
while start <= end:
    Case = (start + end) // 2
    value = (Case + 1) * (n - Case + 1)
    if value == m:
        print("YES")
        quit()
    elif value < m:
        start = Case + 1
    elif value > m:
        end = Case - 1

print("NO")
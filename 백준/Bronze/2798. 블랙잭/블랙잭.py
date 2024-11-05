import sys
input=sys.stdin.readline
import itertools
n, m = map(int, input().split())
arr = list(map(int, input().split()))
Comb = itertools.combinations(arr, 3)
ans = []
for i in Comb:
    ans.append(sum(i))

if m not in ans:
    ans.append(m)
    ans.sort()
    for i in range(len(ans)):
        if ans[i]==m:
            print(ans[i-1])
            break
else:
    print(m)
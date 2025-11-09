import sys
input = sys.stdin.readline
from itertools import combinations

n, k = map(int, input().split())
if k < 5:
    print(0)
    quit()

must = set('antic')
words = []
for _ in range(n):
    words.append(input().strip())

word_sets = []
for w in words:
    word_sets.append(set(w) - must)
#print(word_sets)

candidates = set(chr(i + ord('a')) for i in range(26)) - must

ans = 0
for comb in combinations(candidates, k-5):
    teach = must | set(comb)
    cnt = 0
    for wset in word_sets:
        if wset <= teach:
            cnt += 1
    ans = max(ans, cnt)

print(ans)

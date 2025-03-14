import sys
input = sys.stdin.readline
import math

dic = {0.75 : 0, 0.25 : 0, 0.5 : 0}  
n = int(input())
for _ in range(n):
    a = input().split("/")
    k = int(a[0]) / int(a[1])
    dic[k] += 1

#print(dic)
ans = 0
if dic[0.75] > 0:
    if dic[0.25] > 0:
        if dic[0.75] >= dic[0.25]:
            dic[0.25] = 0
        else:
            dic[0.25] = dic[0.25] - dic[0.75]
ans += dic[0.75]
del dic[0.75]

#print(dic)
if dic[0.25] >= 4:
    ans += dic[0.25] // 4
    dic[0.25] = dic[0.25] % 4

#print(dic)
if dic[0.5] >= 2:
    ans += dic[0.5] // 2
    dic[0.5] = dic[0.5] % 2

#print(dic)
ans += math.ceil(dic[0.5] * 0.5 + dic[0.25] * 0.25)

print(ans)
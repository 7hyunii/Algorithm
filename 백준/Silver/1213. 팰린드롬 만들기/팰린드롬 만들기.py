s = input().strip()
length = len(s)
d = {}
ans = [''] * length

for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1

count = 0
for i in d.values():
    if i % 2 != 0:
        count += 1

if count > 1:
    print("I'm Sorry Hansoo")
    quit()

arr = []
for i, j in d.items():
    arr.append((i, j))

arr.sort(key=lambda x: (x[0]))

left = 0
right = -1
middle = length // 2

for i, j in arr:
    while j > 1:
        ans[left] = i
        ans[right] = i
        left += 1
        right -= 1
        j -= 2
    if j == 1:
        ans[middle] = i

print("".join(ans))
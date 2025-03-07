n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0
visited = set() 

for i in arr:
    if (m - i) in visited:
        count += 1
        visited.remove(m - i)
    else:
        visited.add(i) 

print(count)
paper=[[0 for _ in range(100)] for _ in range(100)]
n=int(input())
for _ in range(n):
    x,y=map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[x+i-1][y+j-1]=1
c=0
for x in range(100):
    for y in range(100):
        c+=paper[x][y]
print(c)

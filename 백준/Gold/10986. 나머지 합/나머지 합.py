import sys
input=sys.stdin.readline
n, m=map(int, input().split())
arr=list(map(int, input().split()))
sum=[0]*n
dic={}
count=0

sum[0]=arr[0]
for i in range(1, n):
    sum[i]=sum[i-1]+arr[i]

for i in range(n):
    sum[i]%=m
    if sum[i]==0:
        count+=1
    mod=sum[i]
    if mod not in dic:
        dic[mod]=1
    else:
        dic[mod]+=1

for i, v in dic.items():
    if v>1:
        count+=(v*(v-1)//2)

print(count)

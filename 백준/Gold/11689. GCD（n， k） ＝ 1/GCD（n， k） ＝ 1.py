#오일러 피 함수
import sys
input=sys.stdin.readline
import math
n=int(input())
ans=n
for i in range(2, int(math.sqrt(n)+1)):
    if n%i==0:                          #소인수 찾기
        ans-=ans/i
        while n%i==0:                   #나머지 소인수만 남기기
            n/=i
if n>1:                                 #남은 소인수 있으면 처리
    ans-=ans/n
print(int(ans))
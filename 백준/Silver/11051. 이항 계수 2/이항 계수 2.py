import sys
import math
input=sys.stdin.readline
a, b= map(int, input().split())
print(math.comb(a, b)%10007)
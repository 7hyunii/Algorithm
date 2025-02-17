import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
print(pow(a, b, 1000000007))    #pow는 분할정복을 활용함
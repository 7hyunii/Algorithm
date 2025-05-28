import sys
input = sys.stdin.readline

n = int(input())

def isPrime(num):
    for i in range(2, int(num**(1/2)+1)):
        if num % i == 0:
            return False
    return True 

visited = []
ans = []
def DFS(num, depth=1):
    visited.append(num)
    if depth == n:
        ans.append(num)

    for i in range(1, 10, 2):    #홀수만 붙여보면 되니까
        node = (num * 10) + i
        if node not in visited and isPrime(node):
            DFS(node, depth+1)

DFS(2)
DFS(3)
DFS(5)
DFS(7)
print(*ans, sep="\n")
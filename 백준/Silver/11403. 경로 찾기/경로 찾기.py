import sys
input = sys.stdin.readline

n = int(input())
Graph = [list(map(int, input().split())) for _ in range(n)]
#print(Graph)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if Graph[i][k] and Graph[k][j]:
                Graph[i][j] = 1

for a in range(n):
    for b in range(n):
        print(Graph[a][b], end=" ")
    print()
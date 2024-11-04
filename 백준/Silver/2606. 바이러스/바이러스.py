from collections import defaultdict

T = defaultdict(list)

def DFS(start, T, visited=[]):
    visited.append(start)
    for node in T[start]:
        if node not in visited:
            DFS(node, T, visited)
    return len(visited)-1

com = int(input())
linked = int(input())
for _ in range(linked):
    a, b = map(int, input().split())
    T[a].append(b)
    T[b].append(a)
#print(T)

print(DFS(1, T))
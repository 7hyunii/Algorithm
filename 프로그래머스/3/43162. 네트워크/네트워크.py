from collections import defaultdict

def solution(n, computers):
    
    Graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                Graph[i+1].append(j+1)
                Graph[j+1].append(i+1)
    
    visited = []
    def DFS(v):
        visited.append(v)
        
        for node in Graph[v]:
            if node not in visited:
                DFS(node)
        
        return visited
    
    answer = 0
    for i in range(1, n+1):
        if i not in visited:
            DFS(i)
            answer += 1
            
    return answer
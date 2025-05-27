
from collections import deque, defaultdict
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    
    Graph = defaultdict(list)
    words += [begin]
    for x in words:
        for y in words:
            if x != y and sum(x != y for x, y in zip(x, y)) == 1:
                Graph[x].append(y)
        
    
    visited = []
    visited.append(begin)
    Q = deque()
    Q.append((begin, 0))
    while Q:
        v, cnt = Q.popleft()
        if v == target:
            return cnt
        for w in Graph[v]:
            if w not in visited:
                Q.append((w, cnt+1))
            
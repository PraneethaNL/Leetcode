from typing import List
from collections import defaultdict,deque

def bfs(edges:List[List[int]],src):

    visited=set()
    que=deque()
    que.append(src)

    #adjacency list for undirected graph
    graph=defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited.add(src)
    bfs=[]
    while que:
        node=que.popleft()
        bfs.append(node)

        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                que.append(child)
    return bfs


    




#QUESTION:

# You are given a directed acyclic graph of 'N' vertices(0 to 'N' - 1) and 'M' weighted edges.

# Return an array that stores the distance(sum of weights) of the shortest path from vertex 0 to all vertices, and 
# if it is impossible to reach any vertex, then assign -1 as distance.

# For Example:
# 'N' = 3, 'M' = 3, 'edges' = [0, 1, 2], [1, 2, 3], [0, 2, 6]].


#ALGO:
#Dijkstra with minheap/priority que as it is


from  typing import *
from collections import defaultdict
from heapq import *

def shortestPathInDAG(n: int, m: int, edges: List[List[int]]) -> List[int]:
    visited=set()
    dist=[-1]*n
    dist[0]=0

    pq=[(0,0)]
    graph=defaultdict(list)
    #adj list
    for u,v,w in edges:
        graph[u].append((v,w))


    while pq:
        d,node=heappop(pq)
        
        if node in visited:
            continue
            #will skip the entire code below
        visited.add(node)
        dist[node]=d
        
        for child, w in graph[node]:
            if child not in visited:
                heappush(pq,(d+w,child))
    return dist

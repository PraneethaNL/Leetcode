#QUESTION:
# You are given an undirected graph with 'N' nodes and 'M' edges. The weight of each edge in the graph is one unit.

# Given a source vertex 'src', you must return an array 'answer' of length 'N', where 'answer[i]' is the shortest path length between the source vertex 'src' and 'i'th vertex.

# Note:
# All the nodes are zero-based.
# Example:
# Input:
# N=5, M=5, edges=[(0, 1), (1, 4), (2, 3), (2, 4), (3, 4)], src=1 
# Output: 1 0 2 2 1

from typing import List
from collections import defaultdict,deque

def shortestPath(n:int, edges: List[List[int]], src:int ) -> List[int]:
    # Write your code here
    dist=[-1]*n
    visited=set()
    q=deque()
    q.append(src)
    visited.add(src)

    adj=defaultdict(list)
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    dist[src]=0
    while q:
        node=q.popleft()
        #visited.add(node)
        for child in adj[node]:
            if child not in visited:
                q.append(child)
                visited.add(child)
                dist[child]=1+dist[node]
        
    return dist
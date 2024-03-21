#QUESTION:
#Find shortest path from a given source vertex to all the other vertices
# You have been given an undirected, connected graph of ‘V’ vertices (labelled from 0 to V-1) and ‘E’ edges.
# Each edge connecting two nodes 'u' and 'v' has a weight denoting the distance between them.

# Your task is to find the shortest path distance from the source node 'S' to all the vertices. 
# You have to return a list of integers denoting the shortest distance between each vertex and source vertex 'S'.


# Note:

# 1. There are no self-loops(an edge connecting the vertex to itself) in the given graph.

# 2. There are no parallel edges i.e no two vertices are directly connected by more than 1 edge.


# For Example:

# Input:
# 4 5
# 0 1 5
# 0 2 8
# 1 2 9
# 1 3 2
# 2 3 6

#ALGO:
#Similar to BFS, instead of a queue we will use a priority queu/ min heap instead.

#TC- O(n log n)

from typing import List
from heapq import *
from collections import defaultdict

def dijkstra(edge: List[List[int]], vertices: int, edges: int, source: int):
    # Write your code here.
    # edge' contains {u, v, distance} vectors.

    #graph will be our adjacency list /hashmap/dictionary:- key is vertex (u) : List of tuples (adjacent vertex (v),weight of the edge b/t u-v)
    graph=defaultdict(list)

    #create an adjacency list from the given graph - edge
    #O( no. of edges)
    for u,v,w in edge:
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    visited=set()
    dist=[0]*vertices

    pq=[(0,source)]

    #O( n log n)
    while pq:
        d,node=heappop(pq)

        if node in visited:
            continue
        visited.add(node)
        dist[node]=d
        for child,w in graph[node]:
            if child not in visited:
                heappush(pq,(d+w,child))
    return dist
#QUESTION:

# Problem statement
# You are given ‘n’ cities, some of which are connected by bidirectional roads. You are also given an ‘n x n’ matrix i.e. ‘roads’, 
#where if city ‘i’ and ‘j’ are connected by a road then ‘roads[i][j]'= 1, otherwise ‘roads[i][j]' = 0.
# A province is a group of cities that are either directly or indirectly connected to each other through roads.
# The goal is to count and return the total number of such provinces in the given matrix.

# So, there are ‘2’ provinces.
# Note:
# 1. A city is connected to itself. So, for every city ‘i’, ‘roads[i][i] = 1’.

# Example:
# n = 4, roads = [ [1, 1, 1, 0],
#                  [1, 1, 1, 0],
#                  [1, 1, 1, 0],
#                  [0, 0, 0, 1] ]

#ALGO:

#created an adjacency list - graph using default dict or list of lists
#followed it by bfs

#TC - O(n) - since we'll visit all the vertices


from typing import List
from collections import defaultdict

def findNumOfProvinces(roads: List[List[int]], n: int) -> int:
    # Write your code here
    visited=[0]*n
    provinces=0

    #adjacency list
    graph=defaultdict(list)
    #graph=[[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if roads[i][j]==1:
                graph[i].append(j)
    print(graph)
    #all the nodes/vertices are disconnected
    #graph will be empty
    #this if statement is not required if you use list of lists for graph
    if not graph:
        return n
    for v in graph:
        if visited[v]==0:
            bfs(v,graph,visited,n)
            provinces+=1
    return provinces

    #2D matrix
    # for i in range(row):
    #     if visited[i]==0:
    #         bfs(i,roads,visited,n)
    #         provinces+=1
    # return provinces

#adjacency list
def bfs(v,graph,visited,n):
    q=[]
    q.append(v)
    visited[v]=1

    while q:
        node=q.pop(0)
        for nei in graph[node]:
            if visited[nei]==0:
                q.append(nei)
                visited[nei]=1

#2D matrix
# def bfs(row,roads,visited,n):
#     q=[]
#     q.append(row)
#     visited[row]=1

#     while q:
#         node=q.pop(0)
#         #traverse the column of this row
#         #col length =n
#         for child in range(n):
#             if roads[node][child]==1 and visited[child]==0:
#                 q.append(child)
#                 visited[child]=1

if __name__ == '__main__':
    # n=4
    # roads=[[1, 1, 1, 0],[1, 1, 1, 0],[1, 1, 1, 0],[0, 0, 0, 1]]
    n = 3
    roads = [ [1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1] ]
    
    count=findNumOfProvinces(roads,n)
    print(count)

	


    

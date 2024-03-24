#QUESTION:
#If we are given a simple directed graph(without weighted edges), return the topological sort of the graph.

#n- no. of edges.
#edges - list of edges


#ALGO:

#Note: the que here will store vertices whose indgreee becomes zero - whether intially or as we progress thru the algo.

#BFS
#We will use indegree list to store the number of incoming edges for each vertex. Intialize to all zeros.
#while creating the adjacency list, we will increase the indegree of each vertex accordingly.
#Similar to our normal bfs, we will append the vertices that have no incoming edges to our que.
#we will pop a node from que and append it to our top order. 
#and we will traverse the neighbhors/childeren of the curr node and decrease their indegree by 1.

from typing import List
from collections import defaultdict,deque

def topological(n:int,edges:List[List[int]])->List[int]:
    #adj list
    graph=defaultdict(list)
    indegree=[0]*n
    top=[]

    for u,v in edges:
        graph[u].append(v)
        indegree[v]+=1

    que=deque()

    for v in range(n):
        if indegree[v]==0:
            que.append(v)

    while que:
        node=que.popleft()
        top.append(node)

        for child in graph[node]:
            indegree[child]-=1
            if indegree[child]==0:
                que.append(child)
    return top





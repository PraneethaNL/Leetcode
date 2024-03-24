#QUESTION:

# You are given a directed acyclic graph of 'N' vertices(0 to 'N' - 1) and 'M' weighted edges.

# Return an array that stores the distance(sum of weights) of the shortest path from vertex 0 to all vertices, and 
# if it is impossible to reach any vertex, then assign -1 as distance.

# For Example:
# 'N' = 3, 'M' = 3, 'edges' = [0, 1, 2], [1, 2, 3], [0, 2, 6]].


#ALGO:
#Dijkstra with minheap/priority que as it is

#TC = O(no. of edges + n logn) , n-no. of vertices

#OR
#Topological sort - This is faster- O(v+e)

# We can compute the topological sort of the DAG and using this order we can modify the distances of each node
#similar to shortest_path_bfs.py 



from  typing import *
from collections import defaultdict,deque
from heapq import *

def shortestPathInDAG(n: int, m: int, edges: List[List[int]]) -> List[int]:

    #DIJKSTRA - O(m+ n log n )

    # visited=set()
    # dist=[-1]*n
    # dist[0]=0

    # pq=[(0,0)]
    # graph=defaultdict(list)
    # #adj list
    # for u,v,w in edges:
    #     graph[u].append((v,w))


    # while pq:
    #     d,node=heappop(pq)
        
    #     if node in visited:
    #         continue
    #         #will skip the entire code below
    #     visited.add(node)
    #     dist[node]=d
        
    #     for child, w in graph[node]:
    #         if child not in visited:
    #             heappush(pq,(d+w,child))
    # return dist

    #TOPOLOGICAL SORT- O(v+e)

    graph=defaultdict(list)
    indegree=[0]*(n)
    
    for u,v,w in edges:
        graph[u].append((v,w))
        indegree[v]+=1
    
    que=deque()
    for v in range(n):
        if indegree[v]==0:
            que.append(v)

    top_ord=[] 
    while que:
        node=que.popleft()
        top_ord.append(node)

        for child,w in graph[node]:
           
            indegree[child]-=1
            if indegree[child]==0:
                que.append(child)
                    
    
    #print(top_ord)
    dist=[float('inf')]*n
    dist[0]=0
   
    inf=10**6

    for node in top_ord:
        for child,w in graph[node]:
            if dist[node]<inf and dist[node]+w<dist[child]:
                dist[child]=dist[node]+w
                

    for node in range(n):
        if dist[node]>inf:
            dist[node]=-1
    return dist


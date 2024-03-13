from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
    def bfs(self,start,adj,visited,parent):
		q=deque()
		q.append(start)
		visited.add(start)
		parent[start]=-1
		while q:
			node=q.popleft()
			for child in adj[node]:
		        if child not in visited: 
		            visited.add(child)
					q.append(child)
					parent[child]=node
		        elif child in visited and child!=parent[node]:
		            return True
	    return False

    def isCycle(self, n: int, adj: List[List[int]]) -> bool:
		#Code here
		visited=set()
		parent=[0]*(n)
		
		for i in range(n):
		    if i not in visited:
		        if self.bfs(i,adj,visited,parent):
		            return True
		return False
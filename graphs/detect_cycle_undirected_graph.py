#QUESTION:
#You are given an undirected graph and we should detect if a cycle exists in the graph.

#AGLO:
#We can slove this using either bfs or dfs.

#BFS Approach:
#We need to find if a node is visited more than once - if it's revisted we should check if it is the parent of the curr node,
#if it is not the parent, it means there is a cycle, 
#draw a sample graph on paper and follow this approach for better understanding.

#we will do normal bfs - intialize a que and send in our starting node,mark it visited 
#and keep appending nodes that are neighbors of this node to the que if they are not visited
#additionally, we will also check if the child/neighbor is visited and if visited then check if the child is the parent of the 
#current node for which we are traversing the for loop/ for which we are checking it's neighbors.

#TC - O(V+E)

from typing import List
from collections import deque

#BFS

class Solution:
    #Function to detect cycle in an undirected graph
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

##DFS

class Solution:
    #Function to detect cycle in an undirected graph
	def dfs(self,start,adj,visited,parent):
		visited.add(start)
		for child in adj[start]:
			if child not in visited:
				#if the child is not visited, then we will do dfs on it
				#since our dfs will return true or false
				#let's put an if on this call
				parent[child]=start
				if self.dfs(child,adj,visited,parent):
					return True
			elif child in visited and child!=parent[start]:
				return True
		return False
		
	
	def isCycle(self, n: int, adj: List[List[int]]) -> bool:
		#Code here
		visited=set()
		parent=[-1]*(n)
		
		for i in range(n):
		    if i not in visited:
		        if self.dfs(i,adj,visited,parent):
		            return True
		return False
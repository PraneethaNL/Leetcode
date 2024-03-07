#QUESTION: 210. Course Schedule II
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
#You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

#ALGO:

#Topological sort and if the len(res) < numcourses then return [] since cycle.

#TC- O(v+E) - Since the bfs visits each vertex once and visits each edge once

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Topological Sort
        #detect if there is a cycle
        #if a node is present more than once in top_order => cycle
        #BFS approach - kahn's algorithm

        graph=defaultdict(list)
        que=[]
        
        indegree=[0]*numCourses
        top_order=[]

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        
        for i in range(numCourses):
            if indegree[i]==0:
                que.append(i)
       
        while que:
            curr=que.pop(0)
            top_order.append(curr)

            for nei in graph[curr]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    que.append(nei)
        #if there is a cycle then len(top_order) will be less than num of courses.
        if len(top_order)<numCourses:
            return []
        return top_order
        
        
#QUESTION: 207. Course Schedule

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

#ALGO:
# Do toplogical sort and if there are duplicates in it then return False.

#TC - O(v+e) v-vertices; e-edges

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Topological Sort
        #detect if there is a cycle
        #if a node is present more than once in top_order => cycle
        #BFS approach - kahn's algorithm
        
        graph=defaultdict(list)
        que=[]

        #indegree list(0->n-1) to store the incoming edges for each node. 
        
        indegree=[0]*numCourses
        top_order=[]

        #create adjacency list
        #and modify the indegrees for each node accordingly

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
        #if length of top_order == no. of courses then 
        #all the nodes/courses are visited
        #if it's less than no. of courses then return false
        return len(top_order)==numCourses
        
        
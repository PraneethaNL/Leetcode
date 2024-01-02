#QUESTION: 

#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
#return the number of islands.

#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
#You may assume all four edges of the grid are all surrounded by water.

#https://leetcode.com/problems/number-of-islands/

#ALGO:

#Use the bfs concept for graphs here
#iterate over each cell and if it's == 1(land) and not already visited, 
#then increment the island count
#apply bfs for the cell - to know if any of it's adjacent nodes are land(1)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        global rows,cols,visited
        
        rows=len(grid)
        cols=len(grid[0])
        
        #will add the visited nodes (row,col) as a tuple to the set

        visited=set()
        count=0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    self.bfs(r,c,grid)
                    count+=1
        return count
    
    def bfs(self,row,col,grid):
        q=[]
        visited.add((row,col))
        q.append((row,col))
        
        # to look for adjacent nodes of the given node in all 4 directions
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while q:
            r,c=q.pop(0)

            for dr,dc in directions:
                r1=r+dr
                c1=c+dc

                if (r1 in range(rows) and c1 in range(cols) and (r1,c1) not in visited and grid[r1][c1] =="1"):
                    q.append((r1,c1))
                    visited.add((r1,c1))

        
                    
                
                
        
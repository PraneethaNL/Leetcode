#Question: Island Perimeter

#https://leetcode.com/problems/island-perimeter/description/

#Algo
#Same as no. of islands problem
#iterate over each cell and if it's == 1(land) and not already visited, 
#then apply bfs for the cell - to know if any of it's adjacent nodes are land(1).
#mind the boundary conditions at line 40,42

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        global rows,cols,visited,perimeter

        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        peri=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    peri=self.bfs(r,c,grid)
                   #visited.add((r,c))
        return peri
    

    def bfs(self,row,col,grid):
        perimeter=0
        q=[]
        q.append((row,col))
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        visited.add((row,col))

        while q:
            r,c=q.pop(0)

            for dr,dc in directions:
                r1=r+dr
                c1=c+dc
                #if the cell is on the edge of the grid
                #it's bounds for row&col will exceed
                if r1<0 or r1 >rows-1:
                    perimeter+=1
                if c1<0 or c1>cols-1:
                    perimeter+=1

                if (r1 in range(rows) and c1 in range(cols) ):
                    if grid[r1][c1]==0:
                        perimeter+=1

                    elif (grid[r1][c1]==1 and (r1,c1) not in visited):
                        q.append((r1,c1))
                        visited.add((r1,c1))
        return perimeter

        
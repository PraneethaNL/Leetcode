#QUESTION:
# Problem statement
# You have been given a grid containing some oranges. Each cell of this grid has one of the three integers values:

# Value 0 - representing an empty cell.
# Value 1 - representing a fresh orange.
# Value 2 - representing a rotten orange.
# Every second, any fresh orange that is adjacent(4-directionally) to a rotten orange becomes rotten.

# Your task is to find out the minimum time after which no cell has a fresh orange. If it's impossible to rot all the fresh oranges then print -1.

# Note:
# 1. The grid has 0-based indexing.
# 2. A rotten orange can affect the adjacent oranges 4 directionally i.e. Up, Down, Left, Right.

#https://www.codingninjas.com/studio/problems/rotting-oranges_701655?leftPanelTabValue=PROBLEM


#TC - O(nxm)


def minTimeToRot(grid, n, m):

    # Write your code here.
    graph=[[] for _ in range(m)]
    visited=set()
    que=[]
    for i in range(n):
        for j in range(m):
            if grid[i][j]==2:
                que.append((i,j))

    dir=[(-1,0),(1,0),(0,1),(0,-1)]
    count=0
    if not que:
        return 0
    #flag=1
    while que:
        length=len(que)
        #first rotten orange
        # if flag:
        #     flag=0
        # else:
        #     count+=1

        #OR

        #increment count normally and return count-1: since we don't have to incerement count at level 0/ first rotten orange.
        
        count+=1
        for _ in range(length):
            r,c=que.pop(0)
           # visited
            visited.add((r,c))
            for rd,cd in dir:
                row=r+rd
                col=c+cd
                if (row in range(n)) and (col in range(m)) and grid[row][col]==1 and (row,col) not in visited:
                    visited.add((row,col))
                    grid[row][col]=2
                    que.append((row,col))

    #if there are any fresh oranges left out         
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                return -1
    #return count
    #to cover the case when there are not rotten oranges
    # if count==0:
    #     return 0
    #we return count-1, because we should npt count at level 0 of the graph
    return count-1

#question : Difference Between Ones and Zeros in Row and Column in a 2D grid.

#https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/?envType=daily-question&envId=2023-12-14

#Algo
# Create two lists to rows and cols.
# rows will store the diff between 1s and 0s for each row in the gievn grid
# i.e., rows[0]= no. of 1s in row0 - no. of 0s in row0 of the given grid.
# Similarly cols will store the diff between 1s and 0s for each column in the given grid.
#res[i][j]=rows[i]+cols[j]
#Insert values into 'res' by using above logic.

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        res=[]

        r=len(grid)
        c=len(grid[0])

        #to store diff b/w 1s and 0s for each row
        rows=[]

        for i in range(r):
            one=grid[i].count(1)
            z=grid[i].count(0)

            rows.append(one-z)
        
        #to store diff b/w 1s and 0s for each col
        cols=[]
        for j in range(c):
            one=0
            z=0
            for i in range(r):
                if grid[i][j]==1:
                    one+=1
                if grid[i][j]==0:
                    z+=1
            cols.append(one-z)
        
        for i in range(r):
            ls=[]
            for j in range(c):
                ls.append(rows[i]+cols[j])
            res.append(ls)
        
        return res



        
        
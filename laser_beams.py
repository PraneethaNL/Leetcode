#QUESTION: Number of Laser Beams in a Bank

#https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2024-01-03

#ALGO:

#Use paper to visualize the matrix and number of beams for one case to get a good idea.

# Calculate the rows, cols for the given matrix.
# If there's only one row, then return 0
# otherwise,
# iterate thru each row and if it has a '1', then call the check function 
# Check function will find the row(that is after the given row) that atleast one '1'
# and count the number of 1's in that row and return the row, count to tha caller.

#We should multiply this count with the number of 1's in the caller and add it to the total count.



class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        global rows,cols
        rows=len(bank)
        if rows<2:
            return 0

        cols=len(bank[0])
        
        total_count=0
        r=0

        for i in range(rows-1):
            
            one_count=bank[i].count("1")
            if one_count:
                r,c=self.check(bank,i+1,rows)
                total_count= total_count+one_count*c
            
            i=r

            #TLE for the below code - 129/147 cases passed
            #this loop will give us TLE,
            #so count 1s as above and then multiply

            # for j in range(cols):
            #     if bank[i][j]=='1':
            #         r,c=self.check(bank,i+1,rows)
            #         total_count+=c
            #i=r
            
        return total_count
                    

    # to check the row that has 1s after the given row i
    # and count the no. of 1's ,because it is = no. of beams.
    def check(self,bank,start,end):
        #print("hi")
        row=-1
        count=0

        for k in range(start,end):
            if '1' in bank[k]:
                row=k
                break
        
        for col in range(cols):
            if bank[row][col]=='1':
                count+=1
        
        return row,count
        




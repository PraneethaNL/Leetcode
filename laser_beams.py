#QUESTION: Number of Laser Beams in a Bank

#https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2024-01-03

#TC- O(n^3)

#TLE for the below code - 128/147 cases passed.

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        global rows,cols
        rows=len(bank)
        
        cols=len(bank[0])
        print(cols)

        total_count=0
        r=0

        for i in range(rows-1):
            print("Hi")
            for j in range(cols):
                if bank[i][j]=='1':
                    r,c=self.check(bank,i+1,rows)
                    total_count+=c
            i=r
        
        return total_count
                    

    # to check the row that has 1s after the given row i
    # and count the no. of 1s = no. of beams
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
        


#QUESTION:

# Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

#https://leetcode.com/problems/perfect-squares/?envType=daily-question&envId=2024-02-08

class Solution:
    def numSquares(self, n: int) -> int:

        #dp stores the min numbers of perfect squares that sum
        #to i for each index i from 1 to n


        dp=[float('inf')]*(n+1)

        #Since there are no squares that sum to 0 (except 0)
        dp[0]=0

        for i in range(1,n+1):
            j=1
            #iterate from 1 to i,provided it's square is <=i
            #till i=j**2 becomes zero, then we'll reach dp[0]
            #whose value we have intialized to 0
            #we need to do plus 1'(+1)' in the recurrsion :dp[i-j**2]+1
            #to account for the number j(which will be part of the sum)
            while j**2<=i:
                dp[i]=min(dp[i],dp[i-j**2]+1)
                j+=1
        
        return dp[n]
        
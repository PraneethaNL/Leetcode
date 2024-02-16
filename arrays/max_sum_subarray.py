#QUESTION: Maximum Subarray

# Given an integer array nums, find the 
# subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

#https://leetcode.com/problems/maximum-subarray/description/

#ALGO:

# Kadane's algortihm
# TC- O(n), space =constant

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's 

        maxi=nums[0]
        sum=0
        for n in nums:
            if sum<0:
                sum=0
            sum+=n
            maxi=max(maxi,sum)
        return maxi
        
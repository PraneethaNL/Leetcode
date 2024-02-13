#QUESTION:
# You are a professional robber planning to rob houses along a street. 
#Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that
#adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# eg:
# nums= [2,1,1,2]
# output = 4
 
#https://leetcode.com/problems/house-robber/description/?envType=daily-question&envId=2024-01-21

#TC - O(n)
#First approch has constant space complexity
#Dp solution has O(n) space complexity

class Solution:
    def rob(self, nums: List[int]) -> int:
        #rob1= amount that was robbed before rob2
        #rob2= amount that is robbed last

        # rob1=0
        # rob2=0
        # length=len(nums)

        # for i in range(length):
        #     curr=max(nums[i]+rob1,rob2)
        #     rob1=rob2
        #     rob2=curr
        
        # return rob2

        #DP solution

        length=len(nums)

        dp=[0]*(length+1)
        dp[1]=nums[0]

        for i in range(1,length):
            dp[i+1] = max(nums[i]+dp[i-1],dp[i])
        
        return dp[length]
            

        
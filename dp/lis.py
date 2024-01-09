#QUESTION: Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence.

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

#https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=daily-question&envId=2024-01-05

#ALGO:

# dp recurrsion:
#while traversing the list from back
# lis[i]=max(lis[i],1+lis[j]) , j:i+1 to length-1

# We will use a list 'lis' that'll store the longest increasing subseq(lis) for every index in nums.
# Intialize the list 'lis' to '1', since the length of lis for each index intially is one(because of itself).

# traverse the list nums in reverse.
# if there are values that are greater than the value at current index in nums[curr:]
# then modify lis[i] to maximum of lis[i] and '1+lis[j]' j is the index which has value > curr index.
#it is 1+lis[j] because, once the if condition is satisfied - it means that the length of lis is alteast
# 1(since curr val itself)+lis[index of element that is > the curr element].

#Time complexity - O(n^2) , Space - O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        length=len(nums)

        lis=[1]*length

        #Traverse the list in reverse

        for i in range(length-1,-1,-1):
            for j in range(i+1,length):
                if nums[i]<nums[j]:
                    #dp equation
                    lis[i]=max(lis[i],1+lis[j])

        return max(lis)        
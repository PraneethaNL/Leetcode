#QUESTION: Maximum product subarray

# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# input=[0,2]
# input=[2,-5,-2,-4,3]

#https://leetcode.com/problems/maximum-product-subarray/description/?source=submission-noac

#ALGO:

# Similar to max_subarray sum, but here we need to keep track of the minimum value aswell.
# Because, the input can contain negative numbers and if the curr value is negative, and the
# curr_min is negative, then curr_min*curr_val can give a bigger value.

# TC- O(n), Space = constant

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max=1
        curr_min=1
        maxi=max(nums)

        for n in nums:
            temp=curr_max*n
            curr_max=max(curr_max*n,curr_min*n,n)
            curr_min=min(temp,curr_min*n,n)
            maxi=max(maxi,curr_max)
        return maxi
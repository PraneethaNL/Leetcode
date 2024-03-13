#QUESTION:
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


#ALGO:

# the second method is faster, as it eliminates use of comb method.

# The intuition behind it:

# let's say I have four 1's
# 1,1,1,1
# for the first 1, I can choose from any of the two ones that are after it = 3
# for the second 1, I will choose the ones that are after it=2
# and for the third one , I wil choose the one that is after it =1

# total = 3+2+1 = 6

# Similar to the idea behind using combinatrics.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq=Counter(nums)

        count=0

        # for _,val in freq.items():
        #     if val>=2:
        #         count+=math.comb(val,2)
        # return count
        
        for num in nums:
            freq[num]-=1
            count+=freq[num]
        return count

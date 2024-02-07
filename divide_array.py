#QUESTION: Divide Array Into Arrays With Max Difference

# You are given an integer array nums of size n and a positive integer k.

# Divide the array into one or more arrays of size 3 satisfying the following conditions:

# Each element of nums should be in exactly one array.
# The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

#https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/?envType=daily-question&envId=2024-02-01

#ALGO:

# sort the given list.
# traverse the list in counts of 2, till the 3rd element from last(length-3).
# assign first,sec,third vars for values at curr,curr+1,curr+2 indices.
# check if third-first is <= k.
# if so, then append them to the result, otherwise return an empty list.

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        res=[]
        nums.sort()
        length=len(nums)

        for i in range(0,length-2,3):
            first=nums[i]
            sec=nums[i+1]
            third=nums[i+2]
                
            if third-first<=k:
                res.append([first,sec,third])
            else:
                return []
        return res



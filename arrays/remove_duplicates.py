#QUESTION:
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

#ALGO:
#two pointers - one holds the location of unique and the other for traversing the array.
#TC= O(n) - left will traverse the entire array.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unq=0
        left=1
        length=len(nums)

        while left<length:
            if nums[unq]==nums[left]:
                left+=1
            #if we find a diff element
            #then increase unq pointer and assign the curr val at that location
            else:
                unq+=1
                nums[unq]=nums[left]
                left+=1
        return unq+1
        
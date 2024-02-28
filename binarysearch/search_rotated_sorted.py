#QUESTION:

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

#ALGO:
#https://www.youtube.com/watch?v=uvB-Ns_TVis&ab_channel=NickWhite

# find the index of smallest element first.
# For which intialize left and right pointers to 0,length-1.
# find the mid and compare it with right. 
# If mid is greater than right - then it's not the normal (ascending order) array.
#     There are smaller values towards the right of mid. So, left = mid+1
# otherwise, if mid element id < right element - then it's normal (in an ascending order array).set
#     so, there can be values lesser than mid to it's left
# do this till left<right
# left will hold the value of smallest element in the array and it is our pivot index.
# After this, we need to find the target in the right sorted array or in the left sorted array wrt ro pivot index.

#TC - O(log n)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Part1 - finding the pivot index
        #for which we need to find the index of smallest element in the list
        #left pointer will be pointing to smallest element after this while loop.

        left=0
        right=len(nums)-1

        while left<right:
            mid = left+(right-left)//2

            #if mid val is > val at right, then the smallest element will
            #be to the left of mid.
            if nums[mid]>nums[right]:
                left=mid+1
            
            #if nums[mid]<=nums[right] - normal increasing order array.
            else:
                right=mid
                

        #Part2 - we have found the pivot index,
        #in rotated sorted array, there are two subarrays that are in increasing order.
        #now we need to find in which subarray our target lies. 

        pivot=left
        #reintialize our pointers.
        left=0
        right=len(nums)-1

        #adjust left and right pointers such that they point to 
        #first and last indices of the subarray that is in increasing order.
        if target>=nums[pivot] and target<=nums[right]:
            left=pivot
        else:
            right=pivot
        
        #normal binary search
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return -1
        
        

        
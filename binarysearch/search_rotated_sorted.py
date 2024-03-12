#QUESTION:

# There is an integer array nums sorted in ascending order ***(with DISTINCT values)***.

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

#ALGO:

#IMP NOTE TO REMEMBER: ONE OF THE HALVES(EITHER TO THE LEFT OF MID OR TO THE RIGHT OF MID) WILL DEFINETLY BE SORTED IN A ROATED SORTED ARRAY.

#https://www.youtube.com/watch?v=uvB-Ns_TVis&ab_channel=NickWhite

#This logic will fail if the array has same elements - eg: [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]

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

#APPROACH 2:
#Go below

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Part1 - finding the pivot index
        #for which we need to find the index of smallest element in the list
        #left pointer will be pointing to smallest element after this while loop.

        left=0
        right=len(nums)-1

        while left<right:
            mid = left+(right-left)//2

            #if mid val is > val at right, then it means there are smaller numbers to the right of mid.
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

#ALGO:
#keep in mind that the elements are all disctinct per the question, if there are similar numbers then we need to tweak this a bit.

#Intuition - the array will have for sure some part of it sorted, either the left of mid or right of mid
# eg: 6,7,0,1,2,4,5 - mid = 1, right of mid is sorted by looking
#to determine this - we compare mid with left and right (bcause in normal sorted array left<mid<right)
#- if left < mid then left side is sorted otherwise right side is sorted ( mid < right)
#so, our idea is to find the the sorted part first - our target need not lie in this sorted part
#so, we determine the sorted half first and then check if our target lies in this sorted half (eg: left <target<mid) or (mid<target<right)
#if it does not lie in the sorted part then it lies in the unsorted part  and we adjust either left or right pointers depending on which sorted
#part we first entered.

#TC - O(logn)

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left =0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2

            if nums[mid]==target:
                return mid

            #if left side is sorted => arr[left]<=arr[mid] - normal ascending order

            if nums[left]<=nums[mid]:
                if nums[left]<=target<=nums[mid]:
                    right=mid-1
                #since target is not in the sorted half
                #got to the right side 
                else:
                    left=mid+1
            #else the right side is sorted
            else:
                if nums[mid]<=target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
            



        
        

        
    
    
        
        

        
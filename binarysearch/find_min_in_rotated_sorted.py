#QUESTION:
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

#ALGO:

#IMP NOTE TO REMEMBER: ONE OF THE HALVES(EITHER TO THE LEFT OF MID OR TO THE RIGHT OF MID) WILL DEFINETLY BE SORTED IN A ROATED SORTED ARRAY.
#we first find the sorted part(either left or right) and then find the min of that.
#then we proceed with the other half of the array.
#In binary search, our logic is to keep eliminating one half every time.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        mini=float("inf")

        while left<=right:
            mid=left+(right-left)//2

            #if left side of mid is the sorted part
            #then nums[left] will be the smallest in that part
            #= is imp, if the arr has 2 elements [2,1] and left =mid
            if nums[left]<=nums[mid]:
                mini=min(mini,nums[left])
                left=mid+1
            #if right of mid is sorted
            else:
                mini=min(mini,nums[mid])
                right=mid-1
        
        return mini

        
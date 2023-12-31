#QUESTION:Kth Largest Element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        
        res=None
        
        #so that we can search the largest element
        #if we just use 'k', then we'll get kth samllest element because it's min heap
        length = len(nums)-k
        
        
        while length:
            heapq.heappop(nums)
            length-=1
        
        return heapq.heappop(nums)
        
#QUESTION:
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem WITHOUT MODIFYING the array nums and uses only CONSTANT EXTRA SPACE.

#ALGO:
#Use slow and fast pointer approach similar to linkedlist cycle detection.


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #Slow and fast pointers approach - O(n) time,O(1) space
        slow=nums[0]
        fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow=nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow
        

        #negate the numbers - modifies the array, TC=O(n)

        #since there are n+1 numbers, the indices will be 0->n
        #we traverse the list and we negate each number at a time
        #which is at index= num
        #if there is a duplicate,then a particular number would have already been
        #negative(because of above)and we will try to negate it again. 
        # for num in nums:
        #     id=abs(num)
        #     if nums[id]<0:
        #         return id
        #     nums[id]=-nums[id]
        # return 0

        # seen=set()

        # for i in nums:
        #     if i not in seen:
        #         seen.add(i)
        #     else:
        #         return i
        # return 0

        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[j]==nums[i]:
        #             return nums[j]
        # return 0

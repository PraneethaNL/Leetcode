#QUESTION:Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.
# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

#ALGO:
#Use a prefix array and postfix array to make it O(n)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #O(n^2)
        # length=len(nums)
        # prod=1
        # res=[]
        # for i in nums:
        #     prod*=i
        
        # for i in range(length):
        #     if nums[i]!=0:
        #         res.append(prod//nums[i])
        #     else:
        #         left=i-1
        #         right=i+1
        #         k=1
        #         while left>=0:
        #             k*=nums[left]
        #             left-=1
        #         while right<length:
        #             k*=nums[right]
        #             right+=1
        #         res.append(k)
        # return res

        #O(n)
        length=len(nums)
        prefix=[1]*length
        postfix=[1]*length
        res=[0]*length

        pref=1
        for i in range(length):
            prefix[i]=pref
            pref*=nums[i]
        
        post=1
        for j in range(length-1,-1,-1):
            postfix[j]=post
            post*=nums[j]

        for i in range(length):
            res[i]=prefix[i]*postfix[i]
        return res

                    


        
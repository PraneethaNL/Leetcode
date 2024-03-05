#QUESTION: Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

#ALGO:
#Moore's voting algorithm can be used. -This technique applies iff the array has majority element.

#Note: the count is not the actual count of the major element in the array, but a place holder.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count=Counter(nums)

        # for key,val in count.items():
        #     if val > len(nums)//2:
        #         return key

        #since majority element always exists
        #moore's voting algo

        majority_element=nums[0]
        count=0
        for i in nums:
            if i==majority_element:
                count+=1
            else:
                count-=1
            if count==0:
                majority_element=i
                count=1
        
        return majority_element

        
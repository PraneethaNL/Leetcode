#QUESTION: Missing Number

#Given an array nums containing n distinct numbers in the range [0, n], 
#return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length=len(nums)
        count=Counter(nums)
        for i in range(length+1):
            if i not in count.keys():
                return i

        #OR, do sum of first n intergers
        # n= len(nums)
        # add = n*(n+1)//2
        # sum_list=sum(nums)

        # return add-sum_list


        
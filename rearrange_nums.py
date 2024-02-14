#QUESTION: Rearrange Array Elements by Sign

# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should rearrange the elements of nums such that the modified array follows the given conditions:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

# Example 1:

# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]

#https://leetcode.com/problems/rearrange-array-elements-by-sign/description/?envType=daily-question&envId=2024-02-14


#ALGO:

# Intialize a list res of length(n), that will store the numbers alternately.
# use two pointers - pos =0, neg=1 for tracking the positions of positive and negative numbers in res
# - which are actually alternate to each other.
#Traverse the given list and assign positive and negative numbers based on their pointer locations.

#TC= O(n)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        length=len(nums)
        res=[0]*length
        pos=0
        neg=1
        for num in nums:
            if num<0:
                res[neg]=num
                neg+=2
            else:
                res[pos]=num
                pos+=2
        return res

        #OR

        # pos=[]
        # neg=[]
        # res=[]
        # for i in nums:
        #     if i>0:
        #         pos.append(i)
        #     else:
        #         neg.append(i)
                
        # length=len(nums)//2
        # for i in range(length):
        #     res.append(pos[i])
        #     res.append(neg[i])
        # return res

        #OR

        # pos=[]
        # neg=[]
        # res=[]
        # for i in nums:
        #     if i>0:
        #         pos.append(i)
        #     else:
        #         neg.append(i)
                
        # length=len(nums)
        # k=0
        # for i in range(0,length,2):
        #     nums[i]=pos[k]
        #     k+=1
        # k=0
        # for i in range(1,length,2):
        #     nums[i]=neg[k]
        #     k+=1
        # return nums




        
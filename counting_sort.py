#QUESTION: Sort Colors

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/798/

#ALGO:

#Counting sort is used : when the values of the elements are in a limited range
# we count the occurrence of each element and modify the array by append values based on this count.
# This is a non comparison sort, with O(n) time complexity in all cases.

#Count number of 0s,1s and 2s.
#Append them to nums, based on their respective counts.


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #counting sort
        
        count=[0]*3
        for i in nums:
            if i==0:
                count[0]+=1
            elif i==1:
                count[1]+=1
            else:
                count[2]+=1
        for i in range(len(nums)):
            if count[0]:
                nums[i]=0
                count[0]-=1
            elif count[1]:
                nums[i]=1
                count[1]-=1
            else:
                nums[i]=2
                count[2]-=1
        
  
        
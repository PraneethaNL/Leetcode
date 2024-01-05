#QUESTION:Minimum Number of Operations to Make Array Empty

# You are given a 0-indexed array nums consisting of positive integers.

# There are two types of operations that you can apply on the array any number of times:

# Choose two elements with equal values and delete them from the array.
# Choose three elements with equal values and delete them from the array.
# Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

# eg:
# nums=[14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]
# expected = 7

#https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/?envType=daily-question&envId=2024-01-04

#ALGO:

#count the frequency of each distinct element in the list : use Counter from collections
#Traverse the frequency dict, if the frequency is =1, then return -1
# else if it's divisible by 3, then number of operations required for this key is =quotient(freq//3)
# if it's remainder is 1 or 2 when divisible by 3 (this case covers the freq divided by 2 aswell)
# then number of operation required = freq//3+ 1

import collections

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        frequency=collections.Counter(nums)
        count=0

        print(frequency)
        
        for key,val in frequency.items():
            if val==1:
                return -1

            if val%3==0:
                count+=val//3
            if val%3==1 or val%3==2:
                count+=val//3+1
            
        
        return count



        
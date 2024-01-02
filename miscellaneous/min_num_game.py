#QUESTION:

#https://leetcode.com/contest/weekly-contest-377/problems/minimum-number-game/


import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        #time complexity : O(n (log n)) for sort + O(n)
        #overall = n log n
        #this is better than the below solution, space wise - no extra space is needed for returing the list
        #and in place swapping

        # length = len(nums)
        # nums.sort()

        # for i in range(0,length-1,2):
        #     nums[i],nums[i+1]=nums[i+1],nums[i]
        
        # return nums

        #OR

        #time complexity : n log n for heapify + n (log n for heapop + O(1) for append)
        #  overall = n log n 
        # Space complexity - O(n) 

        res: List[int]
        res=[]

        heapq.heapify(nums)

        while(nums):
            first= heapq.heappop(nums)
            second = heapq.heappop(nums)

            res.append(second)
            res.append(first)
        
        return res
        
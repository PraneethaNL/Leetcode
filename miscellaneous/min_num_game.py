import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res=[]

        # length = len(nums)
        # nums.sort()

        # for i in range(0,length-1,2):
        #     nums[i],nums[i+1]=nums[i+1],nums[i]
        
        # return nums

        #OR

        heapq.heapify(nums)

        while(nums):
            first= heapq.heappop(nums)
            second = heapq.heappop(nums)

            res.append(second)
            res.append(first)
        
        return res
        
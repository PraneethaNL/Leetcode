
#question

# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        n=len(nums)
        
        for i,val in enumerate(nums):
            left=i+1
            right=n-1
            if i>0 and val==nums[i-1]:
                continue
            while left<right:
                #to avoid same numbers
                
                sum=val+nums[left]+nums[right]
                
                if sum>0:
                    right-=1
                elif sum<0:
                    left+=1
                
                else:
                    res.append([val,nums[left],nums[right]])
                    left+=1
                    #to avoid same numbers 
                    while left <n and nums[left]==nums[left-1]:
                        left+=1
        
        return res
                    
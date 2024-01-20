
#QUESTION:
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

#https://leetcode.com/problems/jump-game/description/

#ALGO:

# if the first element is 0 , then return False,bcause we cannot start at all.
# but if there's only element and length of array is one, then it should be True case. i.e nums=[0]

# if there are no 0's at all in the list, then we will definetly reach the last index(at max we can do one step at a time)
#if there are 0's in between,
# then we will keep track of the max dist/index that we can reach at each index.
# if we encounter 0 at any index and the reach till there is < the index at which we have zero, then
# return false. Because,if the max index that we can reach is less than the index at which we have zero
# we have reached a point where we cannot jump further.

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        length=len(nums)

        if length==1:
            return True

        if nums[0]==0:
            return False
            
        if 0 not in nums:
            return True
        
        else:
            reach=0
            dist=0
            for i,val in enumerate(nums):
                if val!=0:
                    dist=i+val
                    if dist>reach:
                        reach=dist
                    
                elif val==0 and i>=reach and i<length-1:
                    return False
        
        return True
        
       #OR

        #This code is slower compared to the above code on leetcode
        #because if conditions make it faster even though both of them
        #have O(N)


        # length=len(nums)

        # reach=0 # intially the reach is index 0

        # for i in range(length):
        #     if reach<i:
        #         return False
            
        #     reach=max(reach,i+nums[i])
        
        # return True


        


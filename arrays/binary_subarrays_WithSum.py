
#QUESTION:
# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4

#ALGO:

#TLE
#I tried using two for loops - 
#we keep traversing each subarray and if the sum of a subarray exceeds goal, then we need to break from our second loop.
#before that we could increment the pointer of our outer loop, such that the sum becomes equal to goal(i.e we will remove the 1's from left, till sum=goal)



#TLE
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        count=0
        n=len(nums)

        if goal>0:
            i_range=n-goal+1
        else:
            i_range=n
        
        for i in range(i_range):
            sum=0
            for j in range(i,n):
                sum+=nums[j]
                if sum==goal:
                    count+=1
                elif sum>goal:
                    #can rely on this logic, becuase let's say
                    #eg: arr=[1,0,1,0,0,1,1], goal =2
                    #let's say, we are at i=0 and j=5. Our sum=3 exceeds goal, so this while loop will increment i by 1, such that i=1
                    #doubt: will the i get incremented so much that we might miss few subarrays for a pointer before the left pointer i
                    #that we get by the end of this while loop? - No, checked with examples, as soon as we get sum>goal, we'll increment i to make sum=goal
                    while sum>goal:
                        sum-=nums[i]
                        i+=1
                    break
        return count


#O(n)
    
class Solution:

    def atmost(self,nums,goal):
        left=0
        count=0
        sum=0
        n=len(nums)
        #when goal=0, goal-1=-1
        if goal<0:
            return 0
        for j in range(0,n):
            sum+=nums[j]
            if sum>goal:
                while sum>goal:
                    sum-=nums[left]
                    left+=1
            count+=j-left+1
        return count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        return self.atmost(nums,goal)-self.atmost(nums,goal-1)
        

        
        
        
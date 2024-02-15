#QUESTION: Number of Subarrays That Match a Pattern I

# You are given a 0-indexed integer array nums of size n, and a 0-indexed integer array pattern of size m consisting of integers -1, 0, and 1.

# A 
# subarray
#  nums[i..j] of size m + 1 is said to match the pattern if the following conditions hold for each element pattern[k]:

# nums[i + k + 1] > nums[i + k] if pattern[k] == 1.
# nums[i + k + 1] == nums[i + k] if pattern[k] == 0.
# nums[i + k + 1] < nums[i + k] if pattern[k] == -1.
# Return the count of subarrays in nums that match the pattern.

# Example 1:

# Input: nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1]
# Output: 2
# Explanation: Here, the pattern [1,0,-1] indicates that we are looking for a sequence where the first number is smaller than the second, the second is equal to the third, and the third is greater than the fourth. In the array nums, the subarrays [1,4,4,1], and [3,5,5,3] match this pattern.
# Hence, there are 2 subarrays in nums that match the pattern.

#https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/description/

#ALGO:
# We will use an extra list ans - to store the pattern of the given list 'nums'.
# Traverse the given nums list from index 1 -> last and check
# if curr num is <  it's next, then insert '1' to ans
# if curr num is = to it's next num, then insert '0' to ans
# if curr num is > it's next num, then insert -1 to ans

# now, we to find sub lists of length = len(pattern) or m in this ans and check if they match with the given pattern.


#TC - O(n*m) - since the last for loop takes almost O(n) for iterating thru ans
# and the if condition ans[i:i+m] will take O(m) time


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:

        ans=[]
        length=len(nums)
        count=0

        for i in range(1,length):
            if nums[i]<nums[i-1]:
                ans.append(-1)
            elif nums[i]==nums[i-1]:
                ans.append(0)
            elif nums[i]>nums[i-1]:
                ans.append(1)
        
        m= len(pattern)
        for i in range(len(ans)):
            if(ans[i:i+m]==pattern):
                count+=1
        return count

        #OR

        # length_n=len(nums)
        # m=len(pattern)

        # count=0

        # for i in range(length_n-m):
        #     sub =nums[i:i+m+1]
        #     curr=0
        #     for j in pattern:
        #         if j==1 and sub[curr]<sub[curr+1]:
        #             curr+=1
        #         elif j==0 and sub[curr]==sub[curr+1]:
        #             curr+=1
        #         elif j== -1 and sub[curr]>sub[curr+1]:
        #             curr+=1
        #         else:
        #             break
        #     #print(curr)
        #     if curr==m:
        #         count+=1
        
        # return count



        
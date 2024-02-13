#QUESTION:
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

#eg:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
#In this case, the max area of water (blue section) the container can contain is 49.

#ALGO:
# Two pointer approach.
# intialize left = start of the array, right = end of the array
# calculate the area from these pointers
# if height at left < height at right, then move the left pointer towards center.
# else move the right pointer towards center.

#TC- O(n)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1

        res=0

        while left<=right:
            area=(right-left)*min(height[left],height[right])

            #Compare the heights of left and right
            #and move the pointer with lower height towards center
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            res=max(res,area)
        
        return res

        
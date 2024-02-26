#QUESTION: Find Polygon With the Largest Perimeter
# You are given an array of positive integers nums of length n.

# A polygon is a closed plane figure that has at least 3 sides. The longest side of a polygon is smaller than the sum of its other sides.

# Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.

# The perimeter of a polygon is the sum of lengths of its sides.

# Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.


# Input: nums = [1,12,1,2,5,50,3]
# Output: 12
# Explanation: The polygon with the largest perimeter which can be made from nums has 5 sides: 1, 1, 2, 3, and 5. The perimeter is 1 + 1 + 2 + 3 + 5 = 12.

#https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/?envType=daily-question&envId=2024-02-15

#ALGO:

# My Approach:

# Sort the numbers,
# intialize sum=0, to store the sum of the numbers till before index.
# if sum> num at curr index => we have a polygon, compare existing perimeter and sum+i (new perimeter)
# and max of them will be the new perimeter.

# intialize the perimeter =-1, as per question (if not such polygon, then return -1)

#TC - O(n log n):sorting +O(n):iterate thru list = O(n log n)
#Space - constant - O(c)

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        # nums.sort()
        # sum=0
        # peri=-1
        # for i in nums:
        #     if sum<=i:
        #         sum+=i
        #     else:
        #         peri=max(peri,sum+i)
        #         sum=sum+i
        # return peri
    
        # OR
        #Below code is faster, per leetcode
    

        nums.sort(reverse=True)
        maxi=0

        for i in nums:
            maxi=nums.pop(0)
            if maxi < sum(nums):
                return maxi+sum(nums)
        
        return -1

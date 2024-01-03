#QUESTION: Convert an Array Into a 2D Array With Conditions

#You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.

# Note that the 2D array can have a different number of elements on each row.

# Example 1:

# Input: nums = [1,3,4,1,2,3,1]
# Output: [[1,3,4,2],[1,3],[1]]

#ALGO:

#intialize a dictionary 'count' to store the unique values in array with their respective counts/frequencies.
#find the max frequency from the count dict - get key with max value and count[max_value]
#now build the 2D matrix by traversing the dictionary 'rows' no. of time 
#and appending each of it's keys in each iteration to an empty list.
#append this list to result after traversing the dict once.

import collections

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        

        count = collections.Counter(nums)

        #key with max value - i.e, key with max frequency

        max_value= max(count,key=count.get)

        #no. of rows will be = highest frequency in the array
        rows= count[max_value]

        res=[]*rows


        for i in range(rows):
            ls=[]
            for key,val in count.items():
                if val:
                    ls.append(key)
                    count[key]-=1
            res.append(ls)
        
        return res
            
        
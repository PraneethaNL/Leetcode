#QUESTION:
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

#ALGO:
#NOTE
# We are not computing prefix sum of all the indices and storing them before in the dict or list.

# prefsum will store the prefsum till the curr index as the key and the count of each of these prefix sums.

# we put 0:1 in prefsum dict, because we want to consider cases where
# lets say i'm at an index 4 and prefix sum at that index is = k

# so, k-nums[4]=0, which means that the entire subarray from start (index 0) -> index 4 can be considered towards our final count
 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefsum={0:1}
        pref=0

        for num in nums:
            #calculate prefix at curr index
            pref+=num

            #prefix to be removed
            rm=pref-k

            if rm in prefsum:
                count+=prefsum[rm]
            if pref in prefsum:
                prefsum[pref]+=1
            else:
                prefsum[pref]=1
        return count
        
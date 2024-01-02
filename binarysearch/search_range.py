#QUESTION: Search for the range of indices of a given target value in a list of numbers.

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/


#ALGO:

#Binary Search logic.
#Do the normal binary search by intializing left =0, right = len(nums)-1, res=[]
#if mid == target, then we need to tarverse that particular subarray from left to right to find the range.
#in the subarray find the start index of the target
# start will be in range left-> mid.
#append start to result array
#end will be in range start+1 -> right
#append end-1 to the result

#if target is not in array, which implies 'res' is empty then return [-1,-1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left =0
        right = len(nums)-1
        
        res=[]
        
        while left<=right:
            mid= (left+right)//2
            
            if nums[mid]==target:
                start=left
                
                while start<=mid:
                    if nums[start]==target:
                        break
                    else:
                        start+=1
                
                print(start)
                
                res.append(start)
                end =start+1
                while end<=right:
                    if nums[end]==target:
                        end+=1
                    else:
                        break
                        
                res.append(end-1)
                return res
                
            # left sub array
            elif nums[mid]>target:
                right-=1
            
            #mid<target : right sub array
            else:
                left=mid+1
            
        if not res:
            return [-1,-1]
            
            
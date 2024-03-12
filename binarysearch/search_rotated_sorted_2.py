#QUESTION:
# Same as search in rotated sorted array 1, but here we have duplicate elements.

#AGLO:

#IMP NOTE TO REMEMBER: ONE OF THE HALVES(EITHER TO THE LEFT OF MID OR TO THE RIGHT OF MID) WILL DEFINETLY BE SORTED IN A ROATED SORTED ARRAY.


#We'll do search in rotated sorted array, but we encount same elements then we shrink our search space and continue, so that
#we can search in the shrinked rotated sorted array.

#TC-O(n/2)

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            # print(left)

            if nums[mid]==target:
                return True
            
            #handle duplicates
            #shrink our search space
            # if nums[left]==nums[mid]:
            #     left+=1
            #     continue
            # if nums[mid]==nums[right]:
            #     right-=1
            #     continue
            if nums[left]==nums[mid] and nums[mid]==nums[right]:
                left+=1
                right-=1
                #we move on, and try to apply the enitre logic on reduced nums
                continue
            #check if left side is sorted
            if nums[left]<=nums[mid]:
                if nums[left]<=target<=nums[mid]:
                    right=mid-1
                #search the right side
                else:
                    left=mid+1
            #else if the right is sorted
            else:
                if nums[mid]<=target<=nums[right]:
                    left=mid+1
                #check in the left side
                else:
                    right=mid-1
        return False



        
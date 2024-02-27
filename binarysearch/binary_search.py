#binary search code
#to search the index of a given -target in a list

#TC- log n
#Space= O(1), if recurrsion is used then space - log n


def search(self,nums,target):
    right=len(nums)-1
    left=0

    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif target<nums[mid]:
            right=mid-1
        else:
            left=mid+1
    
    return -1
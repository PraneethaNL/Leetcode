#QUESTION:
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


#Dutch-National-Flag (DNF) Problem

#ALGO:
#Use two pointers - for 0's, 2's
#zeroes will be put infront of the list and two's in the end, by doing this 1's will automatically come in between the list
#traverse the list and if you encounter a 0 at index i, swap it with nums[zero] and increment zero and i,
#else if you encounter 2, swap it with nums[two] and decrease two - note we are not incrementing i here, bcause the value at nums[two] 

#TC= O(n)

class Solution:
    def sort012(self,arr):
            # code here
            zero=0
            two=len(arr)-1
            i=0
            
            #using just the for loop will not sort the array properly
            #because i : will go from 0-> end irrespective of two's index
            #which will lead to swapping 1's with 2's since index of two is also decremented.

            # for i in range(len(arr)):
            #     if arr[i]==0:
            #         arr[zero],arr[i]=arr[i],arr[zero]
            #         zero+=1
            #     elif arr[i]==2 and i!=two:
            #         arr[i],arr[two]=arr[two],arr[i]
            #         two-=1
            #     else:
            #         continue

            while i<=two:
                if arr[i]==0:
                    arr[zero],arr[i]=arr[i],arr[zero]
                    zero+=1
                    i+=1
                    
                elif arr[i]==2:
                    arr[i],arr[two]=arr[two],arr[i]
                    two-=1
                else:
                    i+=1
                    
                  
            return arr

#ls=[0,2,1,2,0]
#ls=[0,1,0]
ls=[2,0,2,1,1,0]
sol=Solution()
lsort=sol.sort012(ls)
print(lsort)       
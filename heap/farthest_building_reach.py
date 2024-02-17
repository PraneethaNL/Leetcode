#QUESTION:
# You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

# While moving from building i to building i+1 (0-indexed),

# If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
# If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

# eg:
# Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
# Output: 7
#https://leetcode.com/problems/furthest-building-you-can-reach/description/?envType=daily-question&envId=2024-02-17

#ALGO:
#Use min_heap

#we will traverse the heights list and compare the curr height with next height, if it's greater then
#we need to use either bricks or ladders for it, otherwise we can continue to next index.

#min_heap - no. of elements in the heap at any time = number of ladders.
#if number of elements in the heap are greater than number of ladders
#then we will pop the smallest dist and use bricks for it.
#this way we can ensure that ladders are used for highest distances till that index.
#that are present in heap, smaller distances are popped out.


#TC = O(n log m) , m: len(min_heap) = number of ladders


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        min_heap=[]
        heapify(min_heap)
        length=len(heights)
        
        for i in range(length-1):  # - O(n)
            diff=heights[i+1]-heights[i]

            if diff>0:
                heappush(min_heap,diff) # - log (n)
            else:
                continue

            #if len(heap)>ladders
            #we pop the smallest diff and use bricks for it

            if len(min_heap)>ladders:
                bricks=bricks-heappop(min_heap)   # - log(n)

            #strictly less than zero
            #because if remaining bricks=0, then i+1 should
            #be the return value 
                
            if bricks<0:
                return i
        #default return, end of the list
        return length-1

         


        #I have used an estimate here - if the height diff is > half of 
        #the bricks, then use a ladder 
        #gives wrong answer for 73rd test case
        #72/76 cases- passed

        # dist={}
        # ind=0
        # length=len(heights)
        
        # for i in range(len(heights)-1):
        #     diff = heights[i+1]-heights[i]
        #     if diff>0:
        #         dist[i+1]=diff
        
        # print(dist)

        # for key,val in dist.items():
        #     if ladders and val>bricks//2:
        #         ladders-=1
        #         ind=key
        #     elif bricks and bricks-val>=0:
        #         bricks=bricks-val
        #         ind=key
        #     else:
        #         break
        # for i in range(ind,length-1):
        #     if heights[ind+1]<=heights[ind]:
        #         ind+=1
        #     else:
        #         break
        # return ind
        



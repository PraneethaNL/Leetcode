#QUESTION: Merge overlapping intervals

#https://leetcode.com/problems/merge-intervals/

#ALGO:

#SORT the given intervals based on their START TIME
#res has non ovelapping intervals
#append the interval into result.
#Traverse the intervals: if start of the curr interval is < finish of the interval
# then the curr interval is overlapping with the interval in result.So, merge
#else it is non overlapping and we can simply append it to result and assign the non overlapping index to curr. 


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        #the below line makes the program slower
        #intervals.sort(key = lambda x: x[0])
        result = []
        n = len(intervals)
        index =0
        result.append(intervals[index])
        for m in range(1,n):
            if intervals[m][0]> intervals[index][1]: 
                # means that the interval m does #not overlap with inteval i that is already in result
                result.append(intervals[m])
                index =m
            else:
                #interval m overlaps with interval i 
                intervals[index][1] = max(intervals[index][1],intervals[m][1])
                #intervals[i][0] = min(intervals[i][0],intervals[m][0])
            
        print(result)
        return result

        #OR

        # intervals.sort()
        # res=[]

        # for start,end in intervals:

        #     #if res is empty or start > finish of top entry in res

        #     if not res or res[-1][1]<start:
        #         res.append([start,end])
        

        #if start is < the finish of the last entry and end if > finish 
        #     elif start <= res[-1][1] and end > res[-1][1]:
        #         res[-1][1]=end
        
        # return res


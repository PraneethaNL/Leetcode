#QUESTION:
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

 
#ALGO:
# Code is similar to merge intervals- where we merge overlapping intervals.
# Here since the given intervals are already sorted in increasing order of their start times,
# we need to find the spot - 'i' where we will be inserting our new interval,- start of given intervals, to the end or in between
#depending on where we insert the interval, we will call the merge function
#to merge all the intervals starting from the index 'i-1'(index before the new interval),
#Since intervals before i-1 are all non-overlapping.

#TC- O(n)

#line 46 has O(n) time complexity even tho it is present inside the loop, since we will break off from the loop incase we enter the if condition at lin 43

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        start=newInterval[0]
        ans=[]
        if not intervals:
            ans.append(newInterval)
            return ans

        length=len(intervals)
        #inserting to the end 
        if start>=intervals[length-1][0]:
            intervals.append(newInterval)
            return intervals[:length-1]+self.merge(intervals[length-1:])
        #insert at start
        elif start<=intervals[0][0]:
            intervals.insert(0,newInterval)
            return self.merge(intervals)
        #insert inbetween
        else:
            for i in range(length):
                if intervals[i][0]>start:
                    intervals.insert(i,newInterval)
                    ans=intervals[:i-1]+self.merge(intervals[i-1:])
                    return ans
            
        return ans

    def merge(self,ints):
        res=[]
        #ref is our first non-overlapping interval
        ref=ints[0]
        print(ints)
        length=len(ints)

        for i in range(1,length):
            #curr start < non-overlapping intervals final
            if ints[i][0]<=ref[1]:
                ref[1]=max(ref[1],ints[i][1])
            else:
                res.append(ref)
                ref=[ints[i][0],ints[i][1]]
            if i==length-1:
                res.append(ref)
                
        return res
        

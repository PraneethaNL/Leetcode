#QUESTION: Minimum Number of Arrows to Burst Balloons

#There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

# Example 1:

# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

#ALGO:

#Similar to merge intervals but with some difference, put in on paper to get better idea.
#We need to find the overlapping intervals - but we need to find the overlap time/coordinates at each interval.
#start, end are the starting and end times of out overlapping interval.
#Sort them based on start times and at each interval we will find if the curr interval's 'start-xs' falls in b/w the overlap interval.
#if so we will update the overlap interval start and end.
#otherwise we will increase the count, since the curr intervall does not touch/overlap with the previous overlapping interval's start and end.
#we will update the overlap start and end times to the curr interval's start and end.

#TC- O(n log n)

#NOTE: I have used the word time here, but it can be replaced with co-ordinates.

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count=1
        #we will actually find the overlapping interval
        start=points[0][0]
        end=points[0][1]

        for xs,xe in points:
            #start of curr is in b/w ref interval
            if xs>=start and xs<=end:
                start=max(xs,start)
                end=min(xe,end)
            else:
                count+=1
                start=xs
                end=xe
        return count

        
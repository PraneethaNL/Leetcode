#QUESTION: Meeting Rooms III
# You are given an integer n. There are n rooms numbered from 0 to n - 1.

# You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

# Meetings are allocated to rooms in the following manner:

# Each meeting will take place in the unused room with the lowest number.
# If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
# When a room becomes unused, meetings that have an earlier original start time should be given the room.
# Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

# A half-closed interval [a, b) is the interval between a and b including a and not including b.

 

# Example 1:

# Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
# Output: 0

# Example 2:

# Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
# Output: 1

#ALGO:
#sort meetings based on their start times.
#use a list -count to store the count of number of meetings in each room - count = [0]*n.
#Use two min heaps, one for - to keep track of the rooms that are available
#other - to keep track of the rooms that are busy along with the time when they'll become available (end,room_no.)

#Traverse each meeting and check if the busy list(min-heap) has rooms which finish earlier than the
#current start
#if so, then we will pop them from busy and push them to the available list

#if there are rooms avaialble
#then pop the room with index - we will insert indices of rooms to available list
#and push it to busy list along with finish time

#if no room is available then, we will fetch the room with earliest finish time
#and adjust it's finish time by adding curr meetine interval time and then push it to busy heap with it's room number.

#we will increase the count of room in which current meeting is scheduled/going on 

#TC - O( n log n), Space - O(n)

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        #min-heap to store rooms that are available
        available=[i for i in range(n)]

        #min-heap to store rooms that are busy along with the time
        #when that particular room becomes available - (time,room)
        busy=[]

        #sort meetings based on start time
        #O(n log n)
        meetings.sort()  

        #to store count of meetings for each room
        count=[0]*n

        #O(n)
        for start,end in meetings:
            #if there are rooms that are occupied and 
            #whose meetings finish before the start of curr meeting
            #then we will use them for new meetings, since
            #they have lower index
            while busy and busy[0][0]<=start:
                _,room =heappop(busy)  #O(log (len busy))
                heappush(available,room) 

            if available:
                room=heappop(available)
                heappush(busy,(end,room))

            #if no room is available
            else:
                #pop the min finish time and append curr interval to it
                time,room=heappop(busy)
                heappush(busy,(time+end-start,room))
            
            #increase the count for the room that is available
            #or becomes available earliest
            count[room]+=1
        
        maxi=max(count)

        return count.index(maxi)
            

        
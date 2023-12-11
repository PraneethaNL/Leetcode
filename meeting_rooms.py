class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(intervals):
        # Write your code here

        n=len(intervals)
        intervals.sort(key=lambda x:x[0])
        for i in range(n):
            if intervals[i][1]<=intervals[i+1][0]:
                return False
        
        return True
    
    def min_meeting_rooms(self,intervals):
        # Write your code here
     
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        
        res =0
        count =0
        s,e =0,0
        
        while s<length:
            if start[s]<=end[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            res =max(res,count)
        return res
    

if __name__ =="__main__":
    ints = [(0,30),(5,10),(15,20)]
    sol =Solution()
    rooms = sol.min_meeting_rooms(ints)

    print("min rooms requires =",rooms)

    

    length = len(nums)
        
        for i in range(length):
            nums[i]=[nums[i]-k,nums[i]+k]
        
        count =1
        res =0
        
        nums.sort(key=lambda x:x[1]) 
        
        i=0
        
        for m in range(1,length):
            if nums[m][0]<=nums[i][1]:
                count+=1
                #res =count
            else:
                res = max(res,count)
                i=m
                count =1
                
        
        return res
            
            


    
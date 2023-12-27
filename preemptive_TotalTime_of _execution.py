#QUESTION:Exclusive Time of Functions

#https://leetcode.com/problems/exclusive-time-of-functions/description/


#ALGO:

#Since every function will have a total execution time, let's first intialize the 'res' array which will store the execution times
#to zero.
#We will update the 'res' array for each function call depending upon it's state while considering if it's execution was interrupted.
#We need to use a stack to keep track of the function calls, 
# top of the stack is the id of the function that has started/that is in execution.
# If the state of the function is 'start', we should preempt the prev function in execution and
# update it's execution time so far, in it's corresponding position in the 'res' array.
# 'prev_start_time' will keep track of the actual time when the function that is using the CPU has started.

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res=[0]*n

        fstack=[]
        prev_start_time=0

        for log in logs:
            id,state,time=log.split(":")

            id=int(id)
            time=int(time)

            if state=='start':
                #if a function was already in execution,
                #we are preempting it.
                if fstack:
                    res[fstack[-1]]+=time-prev_start_time

                #append the curr function in execution ( that has started) to top of the stack

                fstack.append(id)
                prev_start_time=time

            #end state
            #+1 since we are counting the total execution time, eg: start =2 and end =5
            #then exection time = 4 (5-2+1)
            else:
                res[fstack.pop()]+=time-prev_start_time+1
                prev_start_time=time+1
        
        return res



                


        
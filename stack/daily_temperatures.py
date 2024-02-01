#QUESTION:
# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

#https://leetcode.com/problems/daily-temperatures/submissions/1162457668/?envType=daily-question&envId=2024-01-31

#ALGO:
# Use a stack to store the indices/days of the temps.
# Intialize an array ans of length =len(temps) with all 0s.
# while traversing the list, check if the curr temp is > the temp of top element in the stack.
#if it is lesser, then pop the index from stack as id and modify the ans[id]=curr_index-id
#continue this until curr_temp is > top element in the stack 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        length=len(temperatures)
        ans=[0]*length

        stack =[]

        for i,val in enumerate(temperatures):

            if not stack:
                stack.append(i)
            else:
                #temps of the indices in stack are in decreasing order
                #temp of top of the stack < curr temp
                #we need to check if stack is not empty,cause if we are at 76 from above example
                #since it's the max element in the list, the entire stack will get popped.
                #and stack[-1] will give index out of range error.
                while stack and temperatures[stack[-1]]<val:
                    id= stack.pop()
                    ans[id]=i-id
                stack.append(i)
        
        return ans




        
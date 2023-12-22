#Question : Longest palindrome substring of a given string
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/

#Algo:
# Traverse the string by considering each element to be center of the plaindrome and
# expand in left & right directions from the index of the current element.

# Time: O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n=len(s)
        res=[]
        res_l=0
        for i in range(n):
            #if the result is of odd length then the below code gives us the 
            #longest palindrome
            left=i
            right=i
            while left>=0 and right<n and s[left]==s[right]:
                if right-left+1>res_l:
                    res_l=right-left+1
                    res=s[left:right+1]
                left-=1
                right+=1
            #if the result is of even length then the below code gives us the 
            #longest palindrome
            left=i
            right=i+1
            while left>=0 and right<n and s[left]==s[right]:
                if right-left+1>res_l:
                    res_l=right-left+1
                    res=s[left:right+1]
                left-=1
                right+=1
        return res
            
        
        
#Question: Given a string s, find the length of the longest substring without repeating characters.

#https://leetcode.com/problems/longest-substring-without-repeating-characters/

#Algo:
#Sliding window, set()

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left=0
        right=0
        n=len(s)
        
        char=set()
        res=0
        while right<n:
            if s[right] not in char:
                char.add(s[right])
                res= max(res,len(char))
                right+=1
            else:
                char.remove(s[left])
                left+=1
        
        return res
                
            
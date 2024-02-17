#QUESTION:  Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 
# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

#https://leetcode.com/problems/minimum-window-substring/description/


#TLE for below code 264/267

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s=len(s)
        len_t=len(t)

        ct=Counter(t)
        res=""
        
        for i in range(0,len_s-len_t+1):
            left=i
            right=i+len_t
            while right<=len_s:
                sub=s[left:right]
                #print(sub)
                cs=Counter(sub)
                count=0
                for key,val in ct.items():
                    if key in cs and cs[key]>=val:
                        count+=1
                    else:
                        break
                if count==len(ct):
                    if not res:
                        res=sub
                        continue
                    if len(sub)<len(res):
                        res=sub
                    break
                right+=1
        return res      


        
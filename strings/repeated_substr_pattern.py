#Question: Repeated Substring Pattern
#Given a string s, check if it can be constructed by taking a substring of it and 
#appending multiple copies of the substring together.

#eg:
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.

#https://leetcode.com/problems/repeated-substring-pattern/

#Algo:
#concatenate the given string with itself as s1.
#remove the first and last chars of s1.
#if s is present in the above pattern, then s can be constructed by repeating a substring of it.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s1=s+s

        n=len(s1)

        if s in s1[1:n-1]:
            return True
        return False

        
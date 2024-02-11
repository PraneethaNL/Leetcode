#QUESTION:Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Example:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

#ALGO:
# This is similar to longest palindromic substring problem.
# We consider each char to be the center of the palindromic substring and traverse on it's both sides
# and check if the chars are same.
# We will introduce a count var, to keep a count of all such substrings.
# we need to do this for both odd length - i.e both left and right pointers start at curr index for odd length substring.
# and for even length substrings - left pointer will be at curr index and right at curr+1.

#TC - O(n^2)

class Solution:
    def countSubstrings(self, s: str) -> int:
        length=len(s)
        res=0
        #Similar to Longest palindromic substring
        for i in range(length):
            #odd length
            res+=self.palindrome(s,i,i)
            #even length
            res+=self.palindrome(s,i,i+1)
                
        return res
    
    def palindrome(self,s,left,right):
        length=len(s)
        count=0
        
        while left>=0 and right <length and s[left]==s[right]:
            count+=1
            left-=1
            right+=1
        return count
        
#QUESTION: Find First Palindromic String in the Array

# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.


#AGLO:

# iterate the list, check if the word is equal to it's reverse.

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word ==word[::-1]:
                return word
            # if self.ispalindrome(word):
            #     return word
        return ""
    
    # def ispalindrome(self,s):
    #     left=0
    #     right=len(s)-1

    #     while left<=right:
    #         if s[left]==s[right]:
    #             left+=1
    #             right-=1
    #         else:
    #             return False
    #     return True
        
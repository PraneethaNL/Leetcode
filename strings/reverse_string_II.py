#QUESTION: Reverse String II

# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# Example 1:

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

#https://leetcode.com/problems/reverse-string-ii/description/

#ALGO:

# Use two pointers approach
# Intialize left =0 and right =K
# you need to add the chars till 'left' and reverse the chars from left to right and
# add the remaining chars from right to the string.

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length =len(s)

        left =0
        right = k

        while left<length:
            s=s[:left]+s[left:right][::-1]+s[right:]

            left=right+k
            right=left+k
        return s
        
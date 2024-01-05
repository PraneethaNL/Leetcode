#QUESTION: Perfect Number
# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

# Given an integer n, return true if n is a perfect number, otherwise return false.
 
# Example 1:

# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.

#https://leetcode.com/problems/perfect-number/

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        root=int(math.sqrt(num))

        div=[]
        val=0
        if num and num!=1:
            div.append(1)

        for i in range(2,root+1):
            if num%i==0:
                div.append(i)
                div.append(num/i)
        print(div)
        val =sum(div)
        return val==num


        
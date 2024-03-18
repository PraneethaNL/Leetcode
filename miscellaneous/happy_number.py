#QUESTION: Happy number
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.



class Solution:
    def isHappy(self, n: int) -> bool:

        
        visited=set()

        if n==1:
            return True

        while n!=1 and n not in visited:
            # digits=[]
            # add=0
            visited.add(n)
            # while n:
            #     rem=n%10
            #     digits.append(rem)
            #     n=n//10
            # for i in digits:
            #     add+=i**2
            s=str(n)
            add=0
            for i in s:
                add+=int(i)**2
            if add==1:
                return True
            else:
                n=add
        
        return False
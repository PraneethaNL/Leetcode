#QUESTION:

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

#ALGO:
#if concatenation of both the strings
#in any order is the same
#it means they are formed by a repeating string.
#we can compute the gcd of their lengths and it will given us the index after which the prefix is repeated.

#TC= log n - since it's log n for computing gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        
        if str1+str2!=str2+str1:
            return ""
        def gcd(a,b):
            #so that a is small and b is big
            if b<a:
                a,b=b,a
            if a==0:
                return b
            else:
                return gcd(b%a,a)
            #Or
            
            # while a:
            #     tmp=a
            #     a=b%a
            #     b=tmp
            # return b

        gcd=gcd(len(str1),len(str2))
        return str1[:gcd]

        # maxi=""

        # if str1+str2==str2+str1:
        #     s=str1+str2
        #     if len(str1)<=len(str2):
        #         small=str1
        #         big=str2
        #     else:
        #         small=str2
        #         big=str1
        #     l1=len(small)
        #     l2=len(big)
        #     for i in range(1,l1+1):
        #         pref=small[:i]
        #         while len(pref)<=l1:
        #             if pref in small:
        #                 pref+=small[:i]
        #             else:
        #                 break
        #         if len(pref)-i==l1:
        #             if l1%i==0 and l2%i==0:
        #                 maxi=small[:i]
        # return maxi
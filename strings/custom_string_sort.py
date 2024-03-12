#QUESTION:

# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

# Example:

# Input:  order = "bcafg", s = "abcd" 

# Output:  "bcad" 

#Leetcode 791:https://leetcode.com/problems/custom-sort-string/description/?envType=daily-question&envId=2024-03-11

#ALGO:
# Intuition:
# keep a counter of frequencies of each char in s.
# We can start traversing the order string one char at a time and if it's present in s, then we will add it to our res- the number of times it's present in s(i.e. freq of char times).

# We will also keep track of the chars that are present only in S and store them in a separate string 'diff'.

# while returning you append this diff either before or after res.

#TC- O(len(s))

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        diff=""
        res=""
        for char in s:
            if char not in order:
                diff+=char

        freq=Counter(s)
        for char in order:
            if char in freq:
                res=res+char*freq[char]
            else:
                continue
              
        if diff:
            res=res+diff
        return res 

    #OR

    #We can use lists aswell for res and diff
    #this is slower than above

    # def customSortString(self, order: str, s: str) -> str:
    #     diff=[]
    #     res=[""]*len(s)
        
    #     for char in s:
    #         if char not in order:
    #             diff.append(char)
    #     i=0
    #     #print(diff)
    #     freq=Counter(s)
    #     for char in order:
    #         if char in freq:
    #             val=freq[char]
    #             while val:
    #                 res[i]=char
    #                 i+=1
    #                 val-=1 
    #         else:
    #             continue     
    #     j=0
    #    # print(res)
    #     while i<len(s):
    #         res[i]=diff[j]
    #         i+=1
    #         j+=1
    
    #     res_s="".join(res)
    #     return res_s          
        
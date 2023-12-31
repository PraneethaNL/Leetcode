
#QUESTION:

# Given an array of strings words, return the words that can be typed using letters of the alphabet 
#on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]

#https://leetcode.com/problems/keyboard-row/description/


class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        r1='qwertyuiop'
        r2='asdfghjkl'
        r3='zxcvbnm'
        res=[]

        for word in words:
            w= word.lower()
            if len(set(r1+w)) == len(r1) or len(set(r2+w))==len(r2) or len(set(r3+w))==len(r3):
                res.append(word)
        
        return res
    
        #OR
        # res=[]

        # for word in words:
        #     val=word.lower()
        #     flag=0
        #     if val[0] in row_wise[0]:
        #         for w in val:
        #             if w not in row_wise[0]:
        #                 flag=1
        #                 break
        #         if not flag:
        #             res.append(word)
        #     if val[0] in row_wise[1]:
        #         for w in val:
        #             if w not in row_wise[1]:
        #                 flag=1
        #                 break
        #         if not flag:
        #             res.append(word)
        #     if val[0] in row_wise[2]:
        #         for w in val:
        #             if w not in row_wise[2]:
        #                 flag=1
        #                 break
        #         if not flag:
        #             res.append(word)
        # return res

        
                    




        
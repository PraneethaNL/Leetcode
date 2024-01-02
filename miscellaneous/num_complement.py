#Question: The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer num, return its complement.

#https://leetcode.com/problems/number-complement/description/


#ALGO:
#convert the given num into binary str
#append the res string by flipping the corresponding bits in the binary str

class Solution:
    def findComplement(self, num: int) -> int:
        num_b= bin(num).replace("0b","")

        res=""

        length=len(num_b)
        for i in range(length):
            if num_b[i]=='0':
                res=res+'1'
            else:
                res=res+'0'
        
        print(res)
        res=int(res,2)

        return res
        

sol=Solution()

sol.findComplement(5)

        
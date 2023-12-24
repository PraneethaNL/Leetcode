#Question: The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#Given two integers x and y, return the Hamming distance between them.

#https://leetcode.com/problems/hamming-distance/

#Algo
#Convert both the numbers into binary
#whichever has the smallest length, fill it's beginning with 0s till both the #binary string become equal
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
    
        xs=bin(x).replace("0b","")
        ys=bin(y).replace("0b","")
        ham_dist=0

        if x<y:
            xs=xs.zfill(len(ys))

        else:
            ys=ys.zfill(len(xs))
        
        for i in range(len(xs)):
            if xs[i]!=ys[i]:
                ham_dist+=1
        
        return ham_dist

#same logic to check for power of any number: instead of 3 use the req number
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        while n%3==0:
            n=n/3
        
        return n==1
    
#if __name__=="__main__":

sol=Solution()

print(sol.isPowerOfThree(10))
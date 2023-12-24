class Solution:
    def canWinNim(self, n: int) -> bool:

        #if n is a multiple of four then ans is False else true
        #ref:https://leetcode.com/problems/nim-game/solutions/3206199/determining-winning-strategy-in-nim-game-using-game-theory/

        if n%4==0:
            return False
        return True
    

if __name__=="__main__":
    sol=Solution()

    print(sol.canWinNim(10))




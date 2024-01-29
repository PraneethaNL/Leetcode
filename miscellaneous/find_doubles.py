#PureStorage

from collections import Counter

class Solution:

    def find_doubles(self,nums:list):
        count=Counter(nums)

        res=[]

        for i in range(501):
            if i in count:
                if i*2 in count and count[i*2]==1:
                    res.append(i)
        
        return res

if __name__=="__main__":
    sol=Solution()
    #ls =[1,2,3,4,5,6,7,8,9,0,8]
    ls=[7,17,11,1,23]

    out= sol.find_doubles(ls)

    print(out)



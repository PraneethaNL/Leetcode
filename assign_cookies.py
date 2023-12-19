#question :Assume you are an awesome parent and want to give your children some cookies. 
# But, you should give each child at most one cookie.
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 
# Your goal is to maximize the number of your content children and output the maximum number.

#Algo:
# Sort the lists in descending order
# start traversing both the lists
# if size of cookie >= greed then increase count and increment pointers in both the lists
# if size of the cookie is less than the greed then increment pointer in greed
# to see if we can satisfy the child with lesser greed with the present size of the cookie

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0

        g.sort(reverse=True)
        s.sort(reverse=True)

        gleft=0
        sleft=0

        while gleft<len(g) and sleft<len(s):
            if s[sleft]>=g[gleft]:
                gleft+=1
                sleft+=1
                count+=1
            
            else:
                gleft+=1
        return count
            
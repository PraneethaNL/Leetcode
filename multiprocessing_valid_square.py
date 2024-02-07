class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        d1=self.distance_square(p1,p2)
        d2=self.distance_square(p1,p3)
        d3=self.distance_square(p1,p4)

        d4=self.distance_square(p2,p3)
        d5=self.distance_square(p2,p4)
        d6=self.distance_square(p3,p4)

        dist=[d1,d2,d3,d4,d5,d6]


        dist=[d1,d2,d3,d4,d5,d6]
        sides={}

        for d in dist:
            if d not in sides:
                sides[d]=1
            else:
                sides[d]+=1
        
        if len(sides)==2 and sides[min(sides.keys())] ==4 and 2*min(sides.values())==max(sides.values()):
            return True
        
        return False
    
    def distance_square(self, p1:list,p2:list):

        dist = (p2[0]-p1[0])**2+(p2[1]-p1[1])**2

        return dist
#QUESTION: Valid Square

# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

# The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

# A valid square has four equal sides with positive length and four equal angles (90-degree angles).

#ALGO:
# Calculate the distance between all the points i.e., total six distances.

# sort these values and first four of them should be same and >0
# remaining two should be equal

#OR instead of sorting we can use a dictionary as below - Which is faster comapared to the sort method.

#We can use a dictionary - to store the distances b/w points 
#insert into dict the count of each distance as the value.
#length of this dict should be 2 and count of smallest key =4 and max_key = min_key*2
#here max_key = diagonal dist and min_key = side of the square.

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
    

        #OR


        # dist.sort()

        # if dist[0]>0 and dist[0]==dist[1]==dist[2]==dist[3] and dist[4]==dist[5]:
        #     #if dist[4]==2*dist[0]:
        #     return True
        # return False

        
        #The below code fails the 00,01,11,12 case

        # print(d1,d2,d3)
        # print(self.distance(p2,p3))

        # if d1==0 or d2==0 or d3==0:
        #     return False
        
        # if d1==d2 and d3== d1*2 and 2*d1 == self.distance(p2,p3):
        #     print("Hello")
        #     return True
        # if d1==d3 and d2== d1*2 and self.distance(p2,p4) == 2*d1:
        #     return True
        # if d2==d3 and d1==d2*2 and self.distance(p4,p3)==2*d2:
        #     return True
        
        # return False

    def distance_square(self, p1:list,p2:list):

        dist = (p2[0]-p1[0])**2+(p2[1]-p1[1])**2

        return dist

        

#Aglo:
#we need to use twp heaps here -  max heap stores smaller elements and 
#min heap stores larger elements

import heapq
class MedianFinder:

    def __init__(self):
        #two heaps
        self.small=[]   #maxheap stores - smaller elements
        #heapq._heapify_max(self.small)
        self.large=[]   #minheap stores -larger elements

    def addNum(self, num: int) -> None:
        #push to maxheap
        #heappush(self.small,num)
        heappush(self.small, -num)
        #max of the smaller elements(max heap) > min of larger elements
        #(min heap)
        #then pop and insert
        if (self.small and self.large and -self.small[0]>self.large[0]):
            #pop from the max heap and push to min heap
            val = heappop(self.small)
            heappush(self.large,-val)

        n1= len(self.small)
        n2=len(self.large)
        
        #uneven length
        if n1-n2>1:
            val = heappop(self.small)
            heappush(self.large,-val)
        if n2-n1>1:
            val = heappop(self.large)
            heappush(self.small,-val)
        


    def findMedian(self) -> float:
        n1= len(self.small)
        n2=len(self.large)

        #length of stream is odd
        if n1>n2:
            print("from max heap")
            return -1*self.small[0]
        if n2>n1:
            print("from min heap")
            return self.large[0]

        print(self.small)
        print(self.large)
        #length of stream in even
        return (-1*self.small[0]+self.large[0])/2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
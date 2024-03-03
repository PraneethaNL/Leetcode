
class QuickSort:
    def partition(self,nums,low,high):
        pivot=nums[high]
        i,j=low,high
        #print(nums)

        while True:
            while i<high:
                print(i)
                print(pivot)
                if nums[i]>nums[pivot]:
                    break
                else:
                    i+=1
            while j>low:
                if nums[j]<nums[pivot]:
                    break
                else:
                    j-=1
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]
            else:
                nums[i],nums[pivot]=nums[pivot],nums[i]
                #exit condition for outer while loop
                return i

    def quicksort(self,nums:list,low,high):

        if low<high:

            pi=self.partition(nums,low,high)
            #print(pi)
            self.quicksort(nums,low,pi-1)
            self.quicksort(nums,pi+1,high)

if __name__=="__main__":
    array = [10, 7, 8, 9, 1, 5]
    n=len(array)
    obj=QuickSort()
    obj.quicksort(array, 0, n - 1)

    print(array)








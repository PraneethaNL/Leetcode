#QUESTION:
# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

#ALGO:

# if the multiplication of row*col of the given matrix != r*c of the reshape matrix, then it is
# not possible to reshape the given matrix, so return it.

# Traverse the given matrix and append each element into a 1D list - flat.
# now iterate this flattend list by appending 'c' number of elements as a list to the result.

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row=len(mat)
        col=len(mat[0])

        if r*c!=row*col:
            return mat
        
        flat=[]

        for num in mat:
            flat+=num
            #use above line instead of extend
            #extend consumes more time
            #flat.extend(num)

        #print(flat)
        
        res=[]
        i=0
        j=0
        while i<r:
            res.append(flat[j:j+c])
            i+=1
            j=j+c
        return res
        



        
        
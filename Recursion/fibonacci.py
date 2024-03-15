
#QUESTION:
# Fibonacci series - 0,1,1,2,3,5,8,13,21...

# every number is the sum of it's two previous numbers, with first two numbers being - 0,1

#calculat the nth fibonacci number.

#ALGO:
#To calculate a fibonacci number we can use recursion or a loop
#The loop solution is way better than the recursion because 
#for recursion the time complexity is - exponential - 2^n  since A(n)=A(n-1)+A(n-2)+1

#O(n)
def fibonacci(n):
    first=0
    sec=1
    k=2
    while k<=n:
        sec=first+sec
        first=sec-first
        k+=1
    return sec

#O(2^n)
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

#We can calculate fibonacci number in O(log n) time
#Using matrix multiplication concept.

#****F(n) = [1 0]*A^n, where matrix A=[[0 1][1 1]].*****

#O(log n) explanation :
#When we know th size of a matrix then multiplying it by itself will take constant time.
#so to compute A^n - will take 'log n' time.
# in first level - we will calculate  A1=A*A  - and we will have n/2 such matrices
#in the next level - we will calulate A2=A1*A1 - n/4 such matrices.
# and so on, till we get one final matrix


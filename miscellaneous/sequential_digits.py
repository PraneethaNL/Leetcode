#QUESTION: Sequential Digits

# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

# Example:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]

#ALGO:
# store '123456789' string in a var num, we will use this since sequential digits will be 
# sub strings of this string.

# get the number of digits of low and high numbers.
# intialize an itr to no. of digits in low and find the substrings of num that are of length itr.
# Append each of them to the res list.
# loop itr till #no. of digits in high, incrementing it by 1 in each iteration.

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        num="123456789"

        res=[]

        l_low=len(str(low))

        l_high=len(str(high))

        itr=l_low

        while itr<=l_high:
            for i in range(9-itr+1):
                val=int(num[i:i+itr])
                if val>=low and val<=high:
                    res.append(val)
            itr+=1
        return res
            

        
#QUESTION: Sort Characters By Frequency

# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

# Example 1:

# Input: s = "tree"
# Output: "eert"

#https://leetcode.com/problems/sort-characters-by-frequency/description/?envType=daily-question&envId=2024-02-07


#ALGO:

#DICT

#Use the Counter method from collections to store the frequency of each char in the string.
# sort this dictionary based on values in decreasing order and type cast it to a dict.
# traverse the sorted dict and append the res based on the count of each char.

#OR - HEAP

#Instead of sorting the dict, insert the elements into a max_heap. Each element of the heap is a tuple (freq_count,char)
#now traverse this max heap, by popping one element at a time and append the char to res based on the count.

# here, I've used min heap itself as a max heap, by inserting the negative value(count) into the heap so that it becomes a max heap.

import heapq
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        res=""
        freq=Counter(s)

        #sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        # for key,val in sorted_freq:
        #     res+=key*val

        # return res

        for key,val in freq.most_common():
            res+=key*val

        return res

        #using max heap

        # max_heap=[]
        # for key,val in freq.items():
        #     heappush(max_heap,(-val,key))

        # while max_heap:
        #     tp=heappop(max_heap)
        #     count=-tp[0]
        #     val=tp[1]
        #     while count:
        #         res+=val
        #         count-=1

        
        # return res
        
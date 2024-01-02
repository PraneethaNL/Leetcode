#QUESTION:
# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.

 
# Example:

# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

#ALGO:

#intialize an empty result list of strs of length n.
#we need to store the indices of scores.
#map the index of each element in score to it's index.
#sort the scores list in descending order.
#traverse the scores and assign the values at the correct index to the result list,
#by getting the index from the map.

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        #Time - O(n log n)
        #Space = O(n)+O(n) =list+dictionary
        #This is faster than below code
        #using dictionary is faster

        length =len(score)

        res=[""]*length
        ind_map={}

        for i in range(length):
            ind_map[score[i]]=i

        score.sort(reverse=True)

        for i in range(length):
            if i==0:
                res[ind_map[score[i]]]="Gold Medal"
            elif i==1:
                res[ind_map[score[i]]]="Silver Medal"
            elif i==2:
                res[ind_map[score[i]]]="Bronze Medal"
            else:
                res[ind_map[score[i]]]= str(i+1)
        return res
    
        #Time - O(n^2) since 'index' method of the list has O(n)        
        # res=list(score)
        # res.sort(reverse=True)
        
        # for i,val in enumerate(res):

        #     ind=score.index(val)
        #     print(ind)
        #     if i==0:
        #         score[ind]='Gold Medal'
        #     elif i==1:
        #         score[ind]='Silver Medal'
        #     elif i==2:
        #         score[ind]='Bronze Medal'
        #     else:
        #         score[ind]=str(i+1)
        
        # return score
    
    
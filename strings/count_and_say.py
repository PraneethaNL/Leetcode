#question
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/4153/
#
#Algo:
#will use an array to store the value for each n
        #value for each 'n' will contain a string representing the count of each digit
        #followed by the digit
        #eg: if dp[1]="11" it means, it has one 1
        #eg: if dp[x]="2234" it means, it is actually 224444

class Solution:
    def countAndSay(self, n: int) -> str:
        
        
        
        dp=[]
        dp.append("1")
        
        for i in range(1,n):
            digit = dp[i-1]
            
            count=1
            length = len(digit)
            sentence=[]
            
            if length ==1:
                say=str(count)+digit
                dp.append(say)
                
            else:
            
                for d in range(0,length):
                    
                    if d==length-1:
                        say=str(count)+digit[d]
                        sentence.append(say)
                        break

                    if digit[d]==digit[d+1]:
                        count+=1
                    else:
                        say=str(count)+digit[d]
                        sentence.append(say)
                        count=1

                    
                if len(sentence)>1:
                    val="".join(sentence)
                else:
                    val=sentence[0]
                    
                dp.append(val)
        
        return dp[n-1]
                    
                    
                
                
        
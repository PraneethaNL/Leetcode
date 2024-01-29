#QUESTION:
# WAP to Count only pure words in the given string
# Input String: “Let’s fight 3together4 4once?”
# Pure words: Let s fight together once
# Output:5

def purewords(s:str):
    
    length=len(s)
    words=[]
    start=0
    for i in range(length):
        
        if not s[i].isalpha():
            #when we have encountered a special immediately at the start of the next iteration 'i'
            #i'm writing this condition for my clarity. We can just skip this if and put
            #start=i+1 outside of the start!=i if statement.
            if start==i:
                start=i+1
            print("not alpha",start,i)
            if start!=i:
                words.append(s[start:i])

                start=i+1
            
    
    print(words)
    print(len(words))
    #return len(res)
        

#string="Let’s fight 3together4 4once?"
string="Hey let's catup after4 sometime?"

purewords(string)


            
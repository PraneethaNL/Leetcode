#QUESTION:

#There is a string “tomorrow”, First o replace with x second “o” replace with xx and third o replace with xxx

def replace_o_with_x(s:str):
    
    length=len(s)
    res=""
    start=0
    count=0


    for  i in range(length):

        if s[i]=='o':
            count+=1
            res+=s[start:i]+"x"*count
            start=i+1
    res+=s[start:length]
    print(res)

string="tomorrow"

replace_o_with_x(string)



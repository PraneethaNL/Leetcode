#QUESTION:

# Put spaces between words starting with a capital letter
# String s = “IAmASoftwareTestEngineer”
# Output- I Am A Software Test Engineer

def insert_space(s:str):

    length=len(s)
    words=[]
    start=0
    for i in range(length):

        #start!=i , because to skip adding s[0:0] i.e, '' to the list
        if s[i].isupper() and start!=i:
            words.append(s[start:i])
            start=i
            

    words.append(s[start:length])
    print(words)
    # char within the "" below is the separator for joining the list-words. Here, i've given space
    # as the char
    res=" ".join(words)
    #res.lstrip()
    print(res)


string="IAmASoftwareTestEngineer"

#string="IamCool"

insert_space(string)

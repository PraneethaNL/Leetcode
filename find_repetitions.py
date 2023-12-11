# import sys

# print(sys.path)

def findrep(short_s,long_s):

    count=0
    pattern=short_s

    while pattern in long_s:
        count+=1
        pattern+=short_s
    
    return count


s1="BB"
s2="ABBBBBBC"

c=findrep(s1,s2)

print(c)

# if __name__== "__main__":
#     c= findrep("BB","ABBBBBBC")

#     print("HI")

# print(c)





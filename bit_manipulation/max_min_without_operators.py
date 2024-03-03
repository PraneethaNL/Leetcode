#Compute max of two numbers without using operators


# def max(n1,n2):
#     #this is simpler and neat
#     val=(n1+n2+abs(a-b))//2
#     return val

#To compute min of two numbers without using comparison operators
def min(a,b):
    maxi=(a+b+abs(a-b))//2
    mini = a+b-maxi
    return mini

# def max(n1,n2):
#     #this logic can be used for both min and max only if numbers are positive
    # also below if check might count as an operator
#     if n1//n2:
#         return n1
#     else:
#         return n2


# def max(n1,n2):
#     s1=bin(n1)
#     s2=bin(n2)
#     # print(s1)
#     # print(s2)

#     i=1

#     while s1[-i] or s2[-i]:
#         if s1[-i]=='b' and s2[-i]=="b":
#             break
#         elif s1[-i]=="b" and s2[-i]!="b":
#             return n2
#         elif s1[-i]!="b" and s2[-i]=="b":
#             return n1
#         i+=1

#     #This is wrong, because we'll traverse from the index = whose value = len(s1) always
#     #if len(s2) is greater then we will few of it's indices from back
#     # for i in range(len(s1),-1,-1):
#     #     if s1[i]=='b' and s2[i]=="b":
#     #         break
#     #     elif s1[i]=="b" and s2[i]!="b":
#     #         return n1
#     #     elif s1[i]!="b" and s2[i]=="b":
#     #         return n2
#     #same length in binary
#     s1=s1.replace("0b","")
#     s2=s2.replace("0b","")

#     for i in range(len(s1)):
#         if s1[i]=="0" and s2[i]=="1":
#             return n2
#         elif s1[i]=="1" and s2[i]=="0":
#             return n1

a=-4
b=-5
maxi=min(a,b)
print(maxi)

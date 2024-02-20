#QUESTION: Rotational Cipher
# One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. 
#Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
# For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". 
#Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). 
#Note that the non-alphanumeric characters remain unchanged.

# Given a string and a rotation factor, return an encrypted string.
# Signature
# string rotationalCipher(string input, int rotationFactor)
# Input
# 1 <= |input| <= 1,000,000
# 0 <= rotationFactor <= 1,000,000
# Output
# Return the result of rotating input a number of times equal to rotationFactor.
# Example 1
# input = Zebra-493?
# rotationFactor = 3
# output = Cheud-726?

#ALGO:

#Traverse the string and if the char is a letter, then capture it's ascii value
#depending on whether it's upper case letter or lower case letter
#for example: if it's an uppercase letter,we need to subtract 65 from it's asci and then add the rotation_factor
#and then find it's remainder with 26.
#else if we just do = asci+rotation_factor, then the final ascii value might be greater than 90('Z') and can refer to non-alpha chars.

def rotationalCipher(input_str, rotation_factor):
  # Write your code here
  
  res=""
  
  for s in input_str:
    if s.isalpha():
      asci=ord(s)
      if s.isupper():
        new=(asci-65+rotation_factor)%26
        res+=chr(65+new)
      else:
        new=(asci-97+rotation_factor)%26
        res+=chr(97+new)
        
    elif s.isdecimal():
      val=int(s)+rotation_factor
      res+=str(val%10)
    else:
      res+=s
  return res


input1="All-convoYs-9-be:Alert1."

val=rotationalCipher(input1,4)
print(val)
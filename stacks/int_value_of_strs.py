#QUESTION:
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=daily-question&envId=2024-01-30

#ALGO:

#Use a stack here.
#Traverse the list 'tokens' and append each non operator value to the stack.
#if we encounter an operator, pop last two elements in the stack and calculate their value by add/sub/mul/div.
#and append this value to the stack.
#return the first (and only) element in the stack as the result.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]

        length=len(tokens)

        ops=["+","-","*","/"]

        for num in tokens:
            if num not in ops:
                stack.append(int(num))
            else:
                sec=stack.pop()
                first=stack.pop()
                if num =="+":
                    val=first+sec
                elif num=="-":
                    val=first-sec
                elif num=="*":
                    val=first*sec
                else:
                    #wrote this for 6/-132 case, but int(first/sec) is
                    #better
                    # if (first <0 and sec >0)or (first>0 and sec<0) :
                    #     val =abs(first)//abs(sec)
                    #     val=-val
                    # else:
                    #     val= first//sec
                    #OR below line is better

                    val=int(first/sec)
                stack.append(val)

        return stack[0]
        
#QUESTION: Linked List Cycle II 

#Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        seen=set()
        while temp:
            if temp in seen:
                return temp
            seen.add(temp)
            temp=temp.next
        return None
        
        
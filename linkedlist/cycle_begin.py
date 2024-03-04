#QUESTION: Linked List Cycle II 

#Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.


#ALGO:
# Approach 2: does not use extra space - intialize fast and slow pointers
# when fast meets slow - cycle is present.
# move slow and head one pointer at a time and their meeting point is the start of the cycle 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Approch 1:

        # temp=head
        # seen=set()
        # while temp:
        #     if temp in seen:
        #         return temp
        #     seen.add(temp)
        #     temp=temp.next
        # return None

        #Approach 2:
        #without extra space
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        #no cycle
        if not fast or not fast.next:
            return None

        temp=head
        #traverse from head and slow simulatneously
        while temp!=slow:
            temp=temp.next
            slow=slow.next
        return slow

        
        
        
        
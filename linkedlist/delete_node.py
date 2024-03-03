#QUESTION:
#Given the head of a linked list, remove the nth node from the end of the list and return its head.

#ALGO:

# Approach without length of the llist:

# we need to traverse till the node before which is to be deleted.
# we will use fast pointer that will travel till n+1 nodes
# now, we move the slow and fast both till fast reaches end of the list - which will take length-n-1 iterations.
# now our slow pointer will point to the node before our node to be deleted.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # temp=head
        # count=0
        # while temp:
        #     count+=1
        #     temp=temp.next
        # #delete head
        # if count==n:
        #     temp=head
        #     head=temp.next
        #     temp.next=None
        #     return head
        # k=count-n-1
        # temp=head
        # while k>0:
        #     temp=temp.next
        #     k-=1
        # prev=temp
        # temp=temp.next
        # prev.next=temp.next
        # temp.next=None

        # return head

        #OR

        fast=head
        slow=head

        for _ in range(n):
            fast=fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            slow=slow.next
            fast=fast.next

        temp=slow.next
        slow.next=slow.next.next
        temp.next=None
        return head
        



        
 
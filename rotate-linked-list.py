#question -https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp=head
        length=0

        temp1=head

        #compute length of the list

        while temp:
            length+=1
            temp=temp.next
        
        if not length or length==1 or k==0:
            return head
        
        k=k%length
        if k==0:
            return head

        # left list : traverse the list till the node before that will be head of the rotated list  
        val= length-k-1

        temp=head

        while val:
            temp=temp.next
            val-=1
        
        head=temp.next
        temp.next=None

        temp=head

        # traverse till end of the right list starting from new head and assign
        #the end of list to the start of the intial list and break (else TLE)
        while temp:
            if not temp.next:
                temp.next=temp1
                break
            else:
                temp=temp.next
        return head


            
        

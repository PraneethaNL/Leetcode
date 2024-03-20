#QUESTION:
# You are given two linked lists: list1 and list2 of sizes n and m respectively.

# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.



# Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [10,1,13,1000000,1000001,1000002,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp=list2
        while temp.next:
            temp=temp.next
        tail=temp

        #since 1<a<=b<<length-1
        # if not a:
        #     head=list2
        # else:
        #     head=list1

        p1=list1
        p2=list1
        a=a-1
        while a or b:
            if a:
                p1=p1.next
                a-=1
            if b:
                p2=p2.next
                b-=1
        tail.next=p2.next
        p1.next=list2
        p2.next=None

        return list1

        #OR
        # ptr=list1

        # for _ in range(a-1):
        #     ptr=ptr.next
        
        # qtr=p1.next

        # for _ in range(b-a+1):
        #     qtr=qtr.next
        
        # ptr.next=list2
        # #iterate till tail of list2
        # while list2.next:
        #     list2=list2.next
        
        # list2.next=qtr

        # return list1

        

        
        
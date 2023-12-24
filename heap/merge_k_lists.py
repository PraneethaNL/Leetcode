#Question: Merge k Sorted Lists

#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#Merge all the linked-lists into one sorted linked-list and return it.

#https://leetcode.com/problems/merge-k-sorted-lists/

#Algo:
#traverse the list and push each element in each list on to a min-heap
#pop from the min heap and add it to a new linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = None

        pq=[]

        n = len(lists)

        for i in range(n):
            temp = lists[i]
            
            while temp:
                heapq.heappush(pq,temp.val)
                temp=temp.next
        
        head= None
        prev =None

        for i in range(len(pq)):

            if not head:
                head=ListNode(heapq.heappop(pq))
                prev=head
            else:
                temp=ListNode(heapq.heappop(pq))
                prev.next=temp
                prev=temp



        return head
            
        

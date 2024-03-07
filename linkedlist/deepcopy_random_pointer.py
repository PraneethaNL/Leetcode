#QUESTION:
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

#ALGO:
#Approach 1:

# Modify the existing list as A->A'->B->B'->C->C'
# Assign random pointers for A',B',C'.
# Iterate the list and separate the new list by adjusting next pointers

#TC= O(n) , Space= Constant

#Approach 2:

#Use a map
#TC - O(n), Space - O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return None
        
        temp=head
        #a->a'->b->b'->c->c'
        while temp:
            nxt=temp.next
            new=Node(temp.val)
            new.next=nxt
            temp.next=new
            temp=nxt
        #assign random pointers for a',b',c'..
        head2=head.next
        prev=head
        while prev:
            rand=prev.random
            if rand:
                prev.next.random=rand.next
            prev=prev.next.next

        #separate the lists and adjust nexts
        prev=head
        curr=head2
        while prev:
            nxt=curr.next
            prev.next=nxt
            if nxt:
                curr.next=nxt.next
            prev=nxt
            if prev:
                curr=prev.next
        return head2
    

    #OR

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return None
        
        #Map

        hash={}
        temp=head

        #create a map to store new nodes
        
        while temp:
            hash[temp]=Node(temp.val)
            temp=temp.next
        
        #traverse list and Assign next and random pointers
        #for it's corresponsding nodes in map

        temp=head
        while temp:
            if temp.next:
                hash[temp].next=hash[temp.next]
            if temp.random:
                hash[temp].random=hash[temp.random]
            temp=temp.next
        return hash[head]




        

        
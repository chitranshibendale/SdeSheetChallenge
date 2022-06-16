"""
https://www.youtube.com/watch?v=VNf6VynfpdM&ab_channel=takeUforward
https://leetcode.com/problems/copy-list-with-random-pointer/
https://www.codingninjas.com/codestudio/problems/873376?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


def cloneRandomList(head):
    iter = head
    front = head
    while iter != None:
        front = iter.next
        copy = LinkedListNode(iter.data)
        iter.next = copy
        copy.next = front
        iter = front
    iter = head
    while iter != None:
        if iter.random != None:
            iter.next.random = iter.random.next
        iter = iter.next.next
    iter = head
    dummy = LinkedListNode(0)
    copy = dummy
    while iter != None:
        front = iter.next.next
        copy.next = iter.next
        iter.next = front
        copy = copy.next
        iter = iter.next
    return dummy.next

#TC : O(n) + O(n) + O(n) = O(3n) = O(n)
#Sc : O(1) [Only extra copylist is created which is not considered in sc)



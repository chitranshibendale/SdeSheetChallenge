"""
https://takeuforward.org/data-structure/remove-n-th-node-from-the-end-of-a-linked-list/
https://www.codingninjas.com/codestudio/problems/799912?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://www.youtube.com/watch?v=Lhu3MsXZy-Q&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=31&ab_channel=takeUforward
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
# TC : O(1)
class LinkedListNode:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next

def deleteNode(node):
    node.data = node.next.data
    node.next = node.next.next

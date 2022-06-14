"""
https://www.youtube.com/watch?v=QfbOhn0WZ88&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=38&ab_channel=takeUforward
https://leetcode.com/problems/linked-list-cycle-ii/
https://www.codingninjas.com/codestudio/problems/1112628?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://takeuforward.org/data-structure/starting-point-of-loop-in-a-linked-list/
"""
#Tc : O(n), SC: (1)
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.pos = []

def firstNode(head):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head
    entry = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            while slow != entry:
                slow = slow.next
                entry = entry.next
            return entry
    return None



def takeInput():
    inputList = [int(i) for i in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head
for _ in range(int(input())):
    head = takeInput()
    pos = int(input())
    print(firstNode(head))
"""
https://www.youtube.com/watch?v=354J83hX7RI&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=34&ab_channel=takeUforward
https://takeuforward.org/data-structure/detect-a-cycle-in-a-linked-list/
https://leetcode.com/problems/linked-list-cycle/
https://www.codingninjas.com/codestudio/problems/628974?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
# Tc : O(n), SC : O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectCycle(head) :
    if head is None:
        return False
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def printLL(head):
    while head is not None:
        print(str(head.data) + "->", end="")
        head = head.next
    print("None")

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

head = takeInput()
pos = int(input())
print(detectCycle(head))
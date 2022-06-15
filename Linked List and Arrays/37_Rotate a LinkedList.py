"""
https://takeuforward.org/data-structure/rotate-a-linked-list/
https://leetcode.com/problems/rotate-list/description/
https://www.codingninjas.com/codestudio/problems/920454?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://www.youtube.com/watch?v=9VPm6nEbVPA&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=40&ab_channel=takeUforward
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def rotate(head, k):
    if head is None or k < 0 or k == 0:
        return head
    curr = head
    length = 1
    while curr.next is not None:
        length += 1
        curr = curr.next
    curr.next = head
    k = k % length
    k = length - k
    while k > 0:
        curr = curr.next
        k -= 1
    head = curr.next
    curr.next = None
    return head


def printLL(head):
    while head is not None:
        print(str(head.data) + "=>", end="")
        head = head.next
    print(None)

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
    k = int(input())
    newhead = rotate(head, k)
    printLL(newhead)
"""
Time Complexity: O(length of list) + O(length of list – (length of list%k))

Reason: O(length of the list) for calculating the length of the list. O(length of the list – (length of list%k)) for breaking link.

Space Complexity: O(1)
"""
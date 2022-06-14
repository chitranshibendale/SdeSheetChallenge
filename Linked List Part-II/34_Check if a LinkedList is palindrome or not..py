"""
https://takeuforward.org/data-structure/check-if-given-linked-list-is-plaindrome/
https://leetcode.com/problems/palindrome-linked-list/
https://www.youtube.com/watch?v=-DtNInqFUXs&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=37&ab_channel=takeUforward
https://www.codingninjas.com/codestudio/problems/799352?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
from sys import stdin


# Following is the class structure of the LinkedListNode class:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    while head is not None:
        fwd = head.next
        head.next = prev
        prev = head
        head = fwd
    return prev

def isPalindrome(head):
    if head is None or head.next is None:
        return True
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    slow.next = reverse(slow.next)
    slow = slow.next
    while slow is not None:
        if head.data != slow.data:
            return False
        head = head.next
        slow = slow.next
    return True


def takeinput():
    inputlist = [int(ele) for ele in input().split()]

    head = None
    tail = None

    for currentData in inputlist:

        if currentData == -1:
            break

        Newnode = Node(currentData)

        if head is None:
            head = Newnode
            tail = Newnode
        else:
            tail.next = Newnode
            tail = Newnode

    return head


# Main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeinput()

    if isPalindrome(head):
        print('true')
    else:
        print('false')

    t -= 1

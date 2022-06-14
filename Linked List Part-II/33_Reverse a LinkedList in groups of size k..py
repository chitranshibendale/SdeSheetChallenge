"""
https://takeuforward.org/data-structure/reverse-linked-list-in-groups-of-size-k/
https://www.codingninjas.com/codestudio/problems/763406?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://www.youtube.com/watch?v=Of0HPkk3JgI&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=34&ab_channel=takeUforward
https://leetcode.com/problems/reverse-nodes-in-k-group/
"""
#tc = O(n/k) * k => O(n), SC : (1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""LEETCODE"""
def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def getListAfterReverseOperation(head, k, b):
    if head == None or k == 1:
        return head
    count = length(head)
    dummy = Node(0)
    dummy.next = head
    curr, nex, prev = dummy, dummy, dummy
    while count >= k:
        curr = prev.next
        nex = curr.next
        for i in range(1, k):
            curr.next = nex.next
            nex.next = prev.next
            prev.next = nex
            nex = curr.next
        prev = curr
        count -= k
    return dummy.next




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
n = int(input())
b = [int(i) for i in input().split()]
printLL(getListAfterReverseOperation(head, n, b))

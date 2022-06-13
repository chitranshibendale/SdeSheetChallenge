class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMiddle(head):
    if head is None:
        return None
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

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

for _ in range(int(input())):
    head = takeInput()
    print(findMiddle(head).data)
"""
Time Complexity: O(N)

Space Complexity: O(1)
"""
"""
https://takeuforward.org/data-structure/find-intersection-of-two-linked-lists/
https://www.youtube.com/watch?v=u4FWXfgS8jw&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=34
https://leetcode.com/problems/intersection-of-two-linked-lists/
https://www.codingninjas.com/codestudio/problems/630457?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
#Time Complexity: O(2*max(length of list1,length of list2))
#Space Complexity: O(1)

from sys import stdin
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findIntersection(firstHead, secondHead):
    if firstHead == None or secondHead == None:
        return -1
    dummy1 = firstHead
    dummy2 = secondHead
    while dummy1 != dummy2:
        if dummy1 is None:
            dummy1 = secondHead
        else:
            dummy1 = dummy1.next
        if dummy2 is None:
            dummy2 = firstHead
        else:
            dummy2 = dummy2.next
    if dummy1 == None:
        return -1
    return dummy1.data



# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1
    return head


def attach(head1, head2):
    temp1 = head1

    while (temp1 != None and temp1.next != None):
        temp1 = temp1.next

    temp2 = head2
    prev = None

    while (temp2.next != None):
        prev = temp2
        temp2 = temp2.next

    if (prev == None):
        if (temp1.data == head2.data):
            temp1.next = head2

    else:
        if (temp2.data == temp1.data):
            prev.next = temp1

        # main


head1 = takeInput()
head2 = takeInput()
head3 = takeInput()

attach(head1, head2)
# Create Intersection
temp1 = head1
while (temp1.next != None):
    temp1 = temp1.next

temp1.next = head3

ans = findIntersection(head1, head2)

print(ans)
"""
https://takeuforward.org/data-structure/merge-two-sorted-linked-lists/
https://www.codingninjas.com/codestudio/problems/800332?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/merge-two-sorted-lists/
"""
# TC : O(n1 + n2), SC : O(1)
import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sortTwoLists(head1, head2):
    if head1 is None and head2 is None:
        return
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data < head2.data:
        forwardHead = head1
        forwardTail = head1
        head1 = head1.next
    else:
        forwardHead = head2
        forwardTail = head2
        head2 = head2.next

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            forwardTail.next = head1
            forwardTail = forwardTail.next
            head1 = head1.next
        else:
            forwardTail.next = head2
            forwardTail = forwardTail.next
            head2 = head2.next
    while head1 is not None:
        forwardTail.next = head1
        forwardTail = forwardTail.next
        head1 = head1.next
    while head2 is not None:
        forwardTail.next = head2
        forwardTail = forwardTail.next
        head2 = head2.next

    return forwardHead



def ll(arr):
    if len(arr) == 0:
        return None

    head = Node(arr[0])
    last = head

    for data in arr[1:]:
        last.next = Node(data)
        last = last.next

    return head


def printll(head):
    while head:
        print(head.data, end=' ')

        head = head.next

    print(-1)


t = int(sys.stdin.readline().strip())

for i in range(t):
    arr1 = list(map(int, sys.stdin.readline().strip().split(" ")))
    arr2 = list(map(int, sys.stdin.readline().strip().split(" ")))

    l1 = ll(arr1[:-1])
    l2 = ll(arr2[:-1])

    l = sortTwoLists(l1, l2)

    printll(l)


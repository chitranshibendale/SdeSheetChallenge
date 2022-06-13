"""
https://www.youtube.com/watch?v=icnp4FJdZ_c&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=32&ab_channel=takeUforward
https://takeuforward.org/data-structure/delete-given-node-in-a-linked-list-o1-approach/
https://www.codingninjas.com/codestudio/problems/1105578?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""
# TC : O(n), SC : O(1)
class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None


def removeKthNode(head, k):
    if head is None:
        return head

    dummy = Node(0)
    dummy.next = head
    fast = dummy
    slow = dummy
    while k != 0:
        fast = fast.next
        k -= 1
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    if slow.next is not None:
        slow.next = slow.next.next
    return dummy.next

def build_linkedList(arr):
    head = None
    for i in range(len(arr)):
        if arr[i] == -1:
            break

        new = Node(arr[i])

        if head is None:
            head = new
            tail = new

        else:
            tail.next = new
            tail = tail.next

    return head

# Main Code.
t = int(input().strip())
for i in range(t):
    k = int(input().strip())
    arr = [int(i) for i in input().strip().split()]

    head = build_linkedList(arr)
    res_head = removeKthNode(head, k)

    while res_head is not None:
        print(res_head.data, end= " ")
        res_head = res_head.next
    print(-1)


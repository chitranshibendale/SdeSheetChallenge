"""
https://www.youtube.com/watch?v=LBVsXSMOIk4&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=33&ab_channel=takeUforward
https://takeuforward.org/data-structure/add-two-numbers-represented-as-linked-lists/
https://leetcode.com/problems/add-two-numbers/
https://www.codingninjas.com/codestudio/problems/add-two-numbers-as-linked-lists_1170520?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
#Time Complexity: O(max(m,n)).
# Assume that m and n represent the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.
#Space Complexity: O(max(m,n)). The length of the new list is at most max(m,n)+1

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

def addTwoNumbers(head1, head2):
    dummy = Node(0)
    temp = dummy
    carry = 0
    while head1 is not None or head2 is not None or carry != 0:
        sum = 0
        if head1 != None:
            sum += head1.data
            head1 = head1.next
        if head2 != None:
            sum += head2.data
            head2 = head2.next

        sum += carry
        carry = sum // 10
        newNode = Node(sum % 10)
        temp.next = newNode
        temp = temp.next
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
    arr = [int(i) for i in input().strip().split()]
    arr1 = [int(i) for i in input().strip().split()]

    head1 = build_linkedList(arr)
    head2 = build_linkedList(arr1)
    res_head = addTwoNumbers(head1, head2)

    while res_head is not None:
        print(res_head.data, end= " ")
        res_head = res_head.next
    print(-1)

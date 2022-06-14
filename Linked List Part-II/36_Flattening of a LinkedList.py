"""
https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1
https://www.codingninjas.com/codestudio/problems/1112655?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://www.youtube.com/watch?v=ysytSSXpAI0&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=39&ab_channel=takeUforward
https://takeuforward.org/data-structure/flattening-a-linked-list/
"""
#TC : O(total nodes)
#SC : O(1)
def merge(h1, h2):
    temp = Node(0)
    result = temp
    while h1 is not None and h2 is not None:
        if h1.data < h2.data:
            temp.bottom = h1
            temp = temp.bottom
            h1 = h1.bottom
        else:
            temp.bottom = h2
            temp = temp.bottom
            h2 = h2.bottom
    if h1:
        temp.bottom = h1
    else:
        temp.bottom = h2
    return result.bottom

def flatten(root):
    if root is None or root.next is None:
        return root
    root.next = flatten(root.next)
    root = merge(root, root.next)
    return root


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None

def printList(node):
    while (node is not None):
        print(node.data, end=" ")
        node = node.bottom

    print()


if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        head = None
        N = int(input())
        arr = []

        arr = [int(x) for x in input().strip().split()]
        temp = None
        tempB = None
        pre = None
        preB = None

        flag = 1
        flag1 = 1
        listo = [int(x) for x in input().strip().split()]
        it = 0
        for i in range(N):
            m = arr[i]
            m -= 1
            a1 = listo[it]
            it += 1
            temp = Node(a1)
            if flag is 1:
                head = temp
                pre = temp
                flag = 0
                flag1 = 1
            else:
                pre.next = temp
                pre = temp
                flag1 = 1

            for j in range(m):
                a = listo[it]
                it += 1
                tempB = Node(a)
                if flag1 is 1:
                    temp.bottom = tempB
                    preB = tempB
                    flag1 = 0
                else:
                    preB.bottom = tempB
                    preB = tempB
        root = flatten(head)
        printList(root)

        t -= 1

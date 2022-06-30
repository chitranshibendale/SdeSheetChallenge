"""
https://takeuforward.org/data-structure/morris-inorder-traversal-of-a-binary-tree/
https://www.youtube.com/watch?v=80Zug6D1_r4&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=39&ab_channel=takeUforward
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
import queue
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preOrder(root):
    curr = root
    ans = []
    while curr != None:
        if curr.left == None:
            ans.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right != None and prev.right != curr:
                prev = prev.right
            if prev.right == None:
                prev.right = curr
                ans.append(curr.val)
                curr = curr.left
            else:
                prev.right = None
                curr = curr.right
    return ans



def takeInput():
    levelOrder = [int(i) for i in input().split()]
    start = 0
    length = len(levelOrder)
    if length == 1:
        return None
    root = BinaryTreeNode(levelOrder[start])
    start += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelOrder[start]
        start += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelOrder[start]
        start += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root

root = takeInput()
print(preOrder(root))

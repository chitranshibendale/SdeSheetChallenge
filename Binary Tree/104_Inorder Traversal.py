"""
https://www.youtube.com/watch?v=lxTGsVXjwvM&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=12&ab_channel=takeUforward
https://leetcode.com/problems/binary-tree-inorder-traversal/
https://takeuforward.org/data-structure/inorder-traversal-of-binary-tree/
"""
import queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    stack = []
    node = root
    inOrder = []
    while True:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            if len(stack) == 0:
                break
            node = stack[-1]
            stack.pop()
            inOrder.append(node.val)
            node = node.right
    return inOrder



def takeInput():
    levelOrder = [int(i) for i in input().split()]
    start = 0
    length = len(levelOrder)
    if length == 1:
        return None
    root = TreeNode(levelOrder[start])
    start += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelOrder[start]
        start += 1
        if leftChild != -1:
            leftNode = TreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelOrder[start]
        start += 1
        if rightChild != -1:
            rightNode = TreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root

root = takeInput()
print(inorderTraversal(root))


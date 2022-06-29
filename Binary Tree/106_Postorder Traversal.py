"""
https://takeuforward.org/data-structure/post-order-traversal-of-binary-tree/
https://www.youtube.com/watch?v=COQOU6klsBg&ab_channel=takeUforward
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    res = []
    stack = []
    cur = root

    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.right
        else:
            cur = stack.pop()
            cur = cur.left
    return res[::-1]




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
print(postorderTraversal(root))

import queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    stack = []
    preOrder = []
    if root is None:
        return preOrder

    stack.append(root)

    while stack:
        node = stack.pop()
        preOrder.append(node.val)
        if node.right != None:
            stack.append(node.right)
        if node.left is not None:
            stack.append((node.left))

    return preOrder





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
print(preorderTraversal(root))

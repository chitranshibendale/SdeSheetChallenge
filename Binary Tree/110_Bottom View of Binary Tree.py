"""
https://takeuforward.org/data-structure/bottom-view-of-a-binary-tree/
https://www.codingninjas.com/codestudio/problems/893110?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1
"""
from sys import stdin, setrecursionlimit
import queue
import sys
from collections import OrderedDict

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bottomView(root):
    ans = []
    if root is None:
        return ans
    d = {}
    q = queue.Queue()
    q.put([root, 0])
    while not q.empty():
        current = q.get()
        node = current[0]
        line = current[1]
        d[line] = node.data

        if node.left != None:
            q.put([node.left, line-1])
        if node.right != None:
            q.put([node.right, line+1])



    for i in sorted(d.items(), key = lambda x:x[0]):
        ans.append(i[1])
    return ans





# Taking level-order input using fast I/O method.
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
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


# Main.
t = int(input())
while t:
    root = takeInput()
    answer = bottomView(root)
    print(*answer)
    t = t - 1

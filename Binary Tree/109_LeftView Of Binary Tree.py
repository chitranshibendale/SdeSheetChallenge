"""
https://www.youtube.com/watch?v=KV4mRzTjlAk&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=26&ab_channel=takeUforward
https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1
https://www.codingninjas.com/codestudio/problems/920519?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def f(root, level, ans):
    if root is None:
        return
    if len(ans) == level:
        ans.append(root.data)
    f(root.left, level+1, ans)
    f(root.right, level+1, ans)

def getLeftView(root)->list:
    ans = []
    f(root, 0, ans)
    return ans


def takeInput():
    lo = [int(i) for i in input().split()]
    if len(lo) == 1:
        return None
    q = queue.Queue()
    start = 0
    root = BinaryTreeNode(lo[start])
    start += 1
    q.put(root)
    while not q.empty():
        cn = q.get()
        lc = lo[start]
        start += 1
        if lc != -1:
            ln = BinaryTreeNode(lc)
            cn.left = ln
            q.put(ln)
        rc = lo[start]
        start += 1
        if rc != -1:
            rn = BinaryTreeNode(rc)
            cn.right = rn
            q.put(rn)
    return root

root = takeInput()
print(getLeftView(root))
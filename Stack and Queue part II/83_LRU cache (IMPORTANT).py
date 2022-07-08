"""
https://www.codingninjas.com/codestudio/problems/670276?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/lru-cache/
"""

from sys import stdin
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    # Initialize the LRU Cache
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = {}
        self.head = Node()
        self.tail = Node()
        self.head.next =self.tail
        self.tail.prev = self.head

    def remove(self, key):
       pred = key.prev
       succ = key.next

       pred.next = succ
       succ.prev = pred

    def insert(self, node):
        pred = self.head
        succ = self.head.next
        pred.next = node
        node.prev = pred

        node.next = succ
        succ.prev = node


    def get(self, key):
        if key in self.d:
            self.remove(self.d[key])
            self.insert(self.d[key])
            return self.d[key].val
        return -1

    def put(self, key, value):
        if key in self.d:
            self.remove(self.d[key])
        newNode = Node(key, value)
        self.d[key] = newNode
        self.insert(self.d[key])

        if len(self.d) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)

            del self.d[lru.key]

    # main


capacity, q = map(int, stdin.readline().rstrip().split(" "))

cache = LRUCache(capacity)

while q != 0:
    query = list(map(int, stdin.readline().rstrip().split()))

    if query[0] == 0:
        key = query[1]
        print(cache.get(key))
    elif query[0] == 1:
        key = query[1]
        value = query[2]
        cache.put(key, value)

    q -= 1
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, val):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(val)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())


    def deQueue(self):
        if self.isEmpty():
            return -1
        return self.s1.pop()

    def peek(self):
        if self.isEmpty():
            return -1
        return self.s1[-1]

    def isEmpty(self):
        return len(self.s1) == 0

# Taking input.
def takeInput():
    n = int(input())

    obstacles = list(map(int, input().strip().split(" ")))

    return obstacles, n

# Main.
q = Queue()
queries = int(input())
while queries:
    values = []
    values = input().split(" ")
    values[0] = int(values[0])
    if values[0] == 1:
        values[1] = int(values[1])
        q.enQueue(values[1])
    elif values[0] == 2:
        print(q.deQueue())
    elif values[0] == 3:
        print(q.peek())
    elif values[0] == 4:
        print(str(q.isEmpty()).lower())
    queries = queries - 1
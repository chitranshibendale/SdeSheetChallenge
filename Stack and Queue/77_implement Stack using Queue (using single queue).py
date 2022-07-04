from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


class Stack:
    def __init__(self):
        self.q = []
        self.count = 0

    def getSize(self):
        return self.count

    def isEmpty(self):
        return ("true" if self.count == 0 else "false")

    def push(self, ele):
        self.q.append(ele)
        for i in range(self.count):
            self.q.append(self.q.pop())
        self.count += 1

    def pop(self):
        if self.count == 0:
            return -1
        self.count -= 1
        return self.q.pop()

    def top(self):
        if self.count == 0:
            return -1
        return self.q[-1]


def takeInput():
    values = list(map(int, stdin.readline().strip().split(" ")))
    return values


#  main
st = Stack()
queries = int(input().strip())
for _ in range(queries):
    values = takeInput()
    if values[0] == 1:
        st.push(values[1])
    elif values[0] == 2:
        print(st.pop())
    elif values[0] == 3:
        print(st.top())
    elif values[0] == 4:
        print(st.getSize())
    else:
        print(st.isEmpty().lower())

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.last = Node()
        self.size = 0

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.last
        self.last = newNode
        self.size += 1
        print("Pushed: ", self.last.data)

    def isEmpty(self):
        if self.last is None:
            return True
        return False

    def pop(self):
        if self.last is None:
            return
        else:
            self.last = self.last.next

    def printAll(self):
        line = ""
        position = self.last
        while position.next is not None:
            line += str(position.data) + " "
            position = position.next
        return line

    def printAsList(self):
        lis = []
        position = self.last
        while position.next is not None:
            position = position.next
            lis.append(position.data)
        print(lis)

    def getSize(self):
        return self.size

    def peek(self):
        return self.last.data


stack = Stack()
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

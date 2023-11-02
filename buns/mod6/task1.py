class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = newNode

    def get(self, index):
        if index < 0:
            return None
        node = self.head
        i = 0
        while node:
            if i == index:
                return node.data
            node = node.next
            i += 1
        return None

    def remove(self, index):
        if index < 0:
            return
        if index == 0:
            if self.head:
                self.head = self.head.next
        node = self.head
        prev = None
        i = 0
        while node and i < index:
            prev = node
            node = node.next
            i += 1
        if node:
            prev.next = node.next

    def insert(self, n, val):
        newNode = Node(val)
        if n == 0:
            newNode.next = self.head
            self.head = newNode
            return
        node = self.head
        prev = None
        i = 0
        while node and i < n:
            prev = node
            node = node.next
            i += 1
        if node:
            prev.next = newNode
            newNode.next = node

    def __iter__(self):
        node = self.head
        while node:
            data = node.data
            node = node.next
            yield data


linkedList = LinkedList()
linkedList.push(1)
linkedList.push(2)
linkedList.push(3)
print(linkedList.get(1))
linkedList.remove(1)
linkedList.insert(1, 4)
for item in linkedList:
    print(item)






class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None

    def len(self):
        pointer = self.head
        length = 1
        while pointer.next != self.head:
            length += 1
            pointer = pointer.next
        return length

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            pointer = self.head
            while pointer.next != self.head:
                pointer = pointer.next
            pointer.next = new_node
            new_node.next = self.head

    def print(self):
        pointer = self.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next
            if pointer == self.head:
                break

    def rnode(self, node):
        if self.head == node:
            pointer = self.head
            while pointer.next != self.head:
                pointer = pointer.next
            pointer.next = self.head.next
            self.head = self.head.next
        else:
            pointer = self.head
            ancestor = None
            while pointer.next != self.head:
                ancestor = pointer
                pointer = pointer.next
                if pointer == node:
                    ancestor.next = pointer.next
                    pointer = pointer.next

    def morreu(self, passo):
        pointer = self.head
        while self.len() > 1:
            c = 1
            while c != passo:
                pointer = pointer.next
                c += 1
            self.rnode(pointer)
            pointer = pointer.next


nc = int(input())
for x in range(1, nc+1):
    cl = CircularList()
    p, k = map(int, input().split())

    for i in range(1, p+1):
        cl.append(i)
    cl.morreu(k)
    print('Case {}:'.format(x), end=' ')
    cl.print()

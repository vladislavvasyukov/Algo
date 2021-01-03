class Node:
    def __init__(self, key=None, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pop_back(self):
        """remove back item"""
        if self.head is None:
            raise Exception("pop_back from empty list")

        if self.head == self.tail:
            key = self.head.key
            self.head = None
            self.tail = None
        else:
            key = self.tail.key
            self.tail = self.tail.prev
            self.tail.next = None

        return key

    def push_back(self, key):
        """add to back"""
        node = Node(key=key)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def add_after(self, node, key):
        """adds key after node"""
        new_node = Node(key=key, next=node.next, prev=node)
        node.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node
        if self.tail == node:
            self.tail = new_node

    def add_before(self, node, key):
        new_node = Node(key=key, next=node, prev=node.prev)
        node.prev = new_node
        if new_node.prev is not None:
            new_node.prev.next = new_node
        if self.head == node:  # is?
            self.head = new_node

    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                print(n.key, end=" ")
                n = n.next
        print()


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.push_back(3)
    dll.push_back(45)
    dll.push_back(0)
    dll.push_back(-4)
    dll.push_back(100)
    dll.push_back(43)
    dll.push_back(19)
    dll.traverse_list()

    dll.pop_back()
    dll.pop_back()
    dll.traverse_list()

    dll.add_before(node=dll.head, key=5)
    dll.add_before(node=dll.head.next.next, key=17)
    dll.add_before(node=dll.tail, key=111)
    dll.traverse_list()

    dll.add_after(node=dll.head, key=22)
    dll.add_after(node=dll.head.next.next, key=234)
    dll.add_after(node=dll.tail, key=56)
    dll.traverse_list()

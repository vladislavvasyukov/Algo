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

class Node:
    def __init__(self, key=None, next_node=None, prev_node=None):
        self.key = key
        self.next_node = next_node
        self.prev_node = prev_node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pop_back(self):
        """remove back item"""
        if self.head is None:
            raise Exception("pop_back from empty list")

        key = self.tail.key
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev_node
            self.tail.next_node = None

        return key

    def push_back(self, key):
        """add to back"""
        node = Node(key=key)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            node.prev_node = self.tail
            self.tail = node

    def add_after(self, node: Node, key):
        """adds key after node"""
        new_node = Node(key=key, next_node=node.next, prev_node=node)
        node.next_node = new_node
        if new_node.next_node is not None:
            new_node.next_node.prev_node = new_node
        if self.tail == node:
            self.tail = new_node

    def add_before(self, node: Node, key):
        new_node = Node(key=key, next_node=node, prev_node=node.prev_node)
        node.prev_node = new_node
        if new_node.prev_node is not None:
            new_node.prev_node.next_node = new_node
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
                n = n.next_node
        print()

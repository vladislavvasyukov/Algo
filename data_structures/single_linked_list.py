from typing import Optional


class Node:
    def __init__(self, key: int = None, next_node=None):
        self.key = key
        self.next_node = next_node


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, key):
        """add to front"""
        node = Node(key=key, next_node=self.head)
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def top_front(self):
        """return from item"""

        if self.head is None:
            raise Exception("top_front from empty list")

        return self.head.key

    def pop_front(self):
        """remove from item"""

        if self.head is None:
            raise Exception("pop_front from empty list")

        key = self.head.key
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None

        return key

    def push_back(self, key):
        """add to back"""
        node = Node(key=key)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def top_back(self):
        """return back item"""

        if self.head is None:
            raise Exception("top_back from empty list")

        return self.tail.key

    def pop_back(self):
        """remove back item"""
        if self.head is None:
            raise Exception("pop_back from empty list")

        if self.head == self.tail:
            key = self.head.key
            self.head = None
            self.tail = None
        else:
            p = self.head
            while p.next_node.next_node is not None:
                p = p.next_node
            key = p.next_node.key
            p.next_node = None
            self.tail = p

        return key

    def find(self, key):
        """is key in list?"""

        current = self.head
        while current is not None:
            if current.key == key:
                return True
            else:
                current = current.next_node

        return False

    def find_node(self, key) -> Optional[Node]:
        current = self.head
        while current is not None:
            if current.key == key:
                return current
            else:
                current = current.next_node

        return None

    def erase(self, key):
        """remove key from list"""

        if self.head is None:
            raise Exception("key is not in list")

        if self.head.key == key:
            self.head = self.head.next_node
            if self.head is None:
                self.tail = None
            return

        current = self.head
        while current.next_node is not None:
            if current.next_node.key == key:
                break
            current = current.next_node

        if current.next_node is None:
            raise Exception("item not found in the list")
        else:
            current.next_node = current.next_node.next_node
            if current.next_node is None:
                self.tail = current

    def empty(self):
        """empty list?"""

        return self.head is None

    def add_before(self, node: Node, key: int):
        """adds key before node"""

        new_node = Node(key=key, next_node=node)

        if self.head == node:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node != node:
                current_node = current_node.next_node

            current_node.next_node = new_node

    def add_after(self, node, key):
        """adds key after node"""
        new_node = Node(key=key, next_node=node.next_node)
        node.next_node = new_node
        if self.tail == node:
            self.tail = new_node

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

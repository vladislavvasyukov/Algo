class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, key):
        """add to front"""
        node = Node(key=key, next=self.head)
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
        self.head = self.head.next
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
            self.tail.next = node
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
            while p.next.next is not None:
                p = p.next
            key = p.next.key
            p.next = None
            self.tail = p

        return key

    def find(self, key):
        """is key in list?"""

        current = self.head
        while current is not None:
            if current.key == key:
                return True
            else:
                current = current.next

        return False

    def erase(self, key):
        """remove key from list"""

        if self.head is None:
            raise Exception("key is not in list")

        if self.head.key == key:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        current = self.head
        while current.next is not None:
            if current.next.key == key:
                break
            current = current.next

        if current.next is None:
            raise Exception("item not found in the list")
        else:
            current.next = current.next.next
            if current.next is None:
                self.tail = current

    def empty(self):
        """empty list?"""

        return self.head is None

    def add_before(self, node, key):
        """adds key before node"""

        new_node = Node(key=key, next=node)

        if self.head == node:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != node is not None:
                current_node = current_node.next

            current_node.next = new_node

    def add_after(self, node, key):
        """adds key after node"""
        new_node = Node(key=key, next=node.next)
        node.next = new_node
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
                n = n.next
        print()

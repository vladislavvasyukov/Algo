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

        current = self.head
        while current.next is not None:
            current = current.next

        return current.key

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

        if self.head is None:
            return False

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

    def empty(self):
        """empty list?"""

        return self.head is None

    def add_before(self, node, key):
        """adds key before node"""

        if self.head == node:
            new_node = Node(key=key, next=self.head)
            self.head = new_node

        elif self.head.next == node:
            new_node = Node(key, next=self.head.next)
            self.head.next = new_node

        else:
            prev_node = self.head
            current_node = self.head.next
            while current_node is not None:
                if current_node == node:
                    break
                prev_node = current_node
                current_node = current_node.next

            if current_node is None:
                raise Exception('Some shit')

            new_node = Node(key=key, next=current_node)
            prev_node.next = new_node


    # def add_before(self, node, key):
    #     if node == self.head.next:
    #         new_node = Node(key=key)
    #         new_node.next = self.head
    #         self.head = new_node
    #         return
    #
    #     current = self.head
    #     while current.next is not None:
    #         if current.next.next == node:
    #             break
    #         current = current.next
    #
    #     new_node = Node(key=key, next=current.next)
    #     current.next = new_node

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


if __name__ == '__main__':
    sl = SingleLinkedList()
    sl.push_back(1)
    sl.push_back(2)
    sl.push_back(3)
    sl.push_back(4)
    sl.push_back(5)
    sl.traverse_list()

    print('\n=============\n')

    el = sl.pop_front()
    print(el)
    sl.traverse_list()

    print('\n=============\n')

    el = sl.pop_back()
    print(el)
    sl.traverse_list()

    print('\n=============\n')

    sl.push_front(100)
    sl.traverse_list()

    print('\n=============\n')

    print(sl.top_front())
    print(sl.top_back())

    print('\n=============\n')

    print(sl.find(100))
    print(sl.find(500))

    print('\n=============\n')

    sl.erase(100)
    sl.traverse_list()

    print('\n=============\n')

    print(sl.empty())

    print('\n=============\n')

    sl.push_front(334)
    sl.push_front(78)
    sl.push_back(96)
    sl.push_back(45)

    sl.traverse_list()

    print()
    print(f'add 66 after = {sl.head.next.next.key}')
    sl.add_after(key=66, node=sl.head.next.next)

    sl.traverse_list()
    print(f'\nadd 15 before = {sl.head.next.key}')
    sl.add_before(key=15, node=sl.head.next)

    sl.traverse_list()

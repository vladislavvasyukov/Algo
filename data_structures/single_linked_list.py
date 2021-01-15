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

    def top_front(self):
        if self.head is None:
            raise Exception
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
            while current_node.next is not None:
                if current_node.next == node:
                    break
                else:
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

    print(sl.top_back())

    print('=====================')

    s4 = SingleLinkedList()
    s4.push_back(56)
    s4.push_back(57)
    s4.push_back(58)
    s4.erase(58)
    print(s4.head.key, s4.tail.key)
    s4.traverse_list()

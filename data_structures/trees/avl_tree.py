# https://blog.coder.si/2014/02/how-to-implement-avl-tree-in-python.html

class AvlNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)


class AvlTree:

    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    def insert(self, key):
        n = AvlNode(key)

        if not self.node:
            self.node = n
            self.node.left = AvlTree()
            self.node.right = AvlTree()

        elif key < self.node.key:
            self.node.left.insert(key)

        elif key > self.node.key:
            self.node.right.insert(key)

        self.rebalance()

    def rebalance(self):
        self.update_heights(recursive=False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()

                self.rotate_right()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()  # we're in case III
                    self.update_heights()
                    self.update_balances()

                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()

            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else:
            self.height = -1

    def update_balances(self, recursive=True):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def rotate_right(self):
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def rotate_left(self):
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    def delete(self, key):
        if self.node is not None:
            if self.node.key == key:
                if not self.node.left.node and not self.node.right.node:
                    self.node = None

                elif not self.node.left.node:
                    self.node = self.node.right.node

                elif not self.node.right.node:
                    self.node = self.node.left.node
                else:
                    successor = self.node.right.node
                    while successor and successor.left.node:
                        successor = successor.left.node

                    if successor:
                        self.node.key = successor.key
                        self.node.right.delete(successor.key)

            elif key < self.node.key:
                self.node.left.delete(key)

            elif key > self.node.key:
                self.node.right.delete(key)

            self.rebalance()

    def inorder_traverse(self):
        result = []

        if not self.node:
            return result

        result.extend(self.node.left.inorder_traverse())
        result.append(self.node.key)
        result.extend(self.node.right.inorder_traverse())

        return result

    def display(self, node=None, level=0):
        if not node:
            node = self.node

        if node.right.node:
            self.display(node.right.node, level + 1)
            print('\t' * level, '    /')

        print('\t' * level, node)

        if node.left.node:
            print('\t' * level, '    \\')
            self.display(node.left.node, level + 1)


if __name__ == "__main__":
    tree = AvlTree()
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    for key in data:
        tree.insert(key)

    tree.display()

    for key in [4, 3]:
        tree.delete(key)

    print(tree.inorder_traverse())
    tree.display()

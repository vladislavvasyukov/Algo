from .binary_search_tree import BinarySearchTree


class SplayTree(BinarySearchTree):

    def splay(self, node):
        while node.parent is not None:
            if node.parent.parent is None:
                if node.is_left_child():
                    # zig rotation
                    self.right_rotate(node.parent)
                else:
                    # zag rotation
                    self.left_rotate(node.parent)
            elif node.is_left_child() and node.parent.is_left_child():
                # zig-zig rotation
                self.right_rotate(node.parent.parent)
                self.right_rotate(node.parent)
            elif node.is_right_child() and node.parent.is_right_child():
                # zag-zag rotation
                self.left_rotate(node.parent.parent)
                self.left_rotate(node.parent)
            elif node.is_right_child() and node.parent.is_left_child():
                # zig-zag rotation
                self.left_rotate(node.parent)
                self.right_rotate(node.parent)
            else:
                # zag-zig rotation
                self.right_rotate(node.parent)
                self.left_rotate(node.parent)

    def left_rotate(self, node):
        y = node.right_child
        node.right_child = y.left_child
        if y.left_child is not None:
            y.left_child.parent = node

        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node.is_left_child():
            node.parent.left_child = y
        else:
            node.parent.right_child = y
        y.left_child = node
        node.parent = y

    def right_rotate(self, node):
        y = node.left_child
        node.left_child = y.right_child
        if y.right_child is not None:
            y.right_child.parent = node

        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node.is_right_child():
            node.parent.right_child = y
        else:
            node.parent.left_child = y

        y.right_child = node
        node.parent = y

    def find(self, key):
        n = super().find(key)
        self.splay(n)
        return n

    def put(self, key, value=None):
        super().put(key, value)
        self.find(key)

    def remove(self, current_node):
        self.splay(current_node.next())
        self.splay(current_node)
        super().remove(current_node)


if __name__ == '__main__':
    ...

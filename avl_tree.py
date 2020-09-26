from binary_search_tree import BinarySearchTree, TreeNode


class AVLTreeNode(TreeNode):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.balance_factor = 0


class AVLTree(BinarySearchTree):
    @staticmethod
    def create_node(key, value, parent=None):
        return AVLTreeNode(key, value, parent=parent)

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = self.create_node(key, value, current_node)
                self.update_balance(current_node.left_child)
        elif key > current_node.key:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = self.create_node(key, value, current_node)
                self.update_balance(current_node.right_child)
        else:
            current_node.value = value

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
            self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
            self.rotate_right(node)

    def rotate_left(self, old_root):
        new_root = old_root.right_child
        old_root.right_child = new_root.left_child

        if new_root.has_left_child():
            new_root.left_child.parent = old_root

        new_root.parent = old_root.parent
        if old_root.is_root():
            self.root = new_root
        else:
            if old_root.is_left_child():
                old_root.parent.left_child = new_root
            else:
                old_root.parent.right_child = new_root

        new_root.left_child = old_root
        old_root.parent = new_root
        old_root.balance_factor = old_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(old_root.balance_factor, 0)


if __name__ == '__main__':
    tree = AVLTree()
    tree[30] = "red"
    tree[4] = "blue"
    tree[6] = "yellow"
    tree[2] = "at"
    tree[8] = 'df'
    tree.print_yourself()
    tree[45] = "as"
    tree[32] = "asd"
    tree[31] = "aaa1"
    tree[33] = "aaa2"
    tree[34] = "aaa3"
    tree[3] = "aaa3"
    tree[48] = 'as'
    tree[47] = 'asdf'

    tree.print_yourself()

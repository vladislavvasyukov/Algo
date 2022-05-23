class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def __iter__(self):
        if self:
            if self.has_left_child():
                yield from self.left_child

            yield self.key

            if self.has_right_child():
                yield from self.right_child

    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not (self.has_left_child() or self.has_right_child())

    def has_any_children(self):
        return self.has_left_child() or self.has_right_child()

    def has_both_children(self):
        return self.has_left_child() and self.has_right_child()

    def replace_node_data(self, node):
        self.key = node.key
        self.value = node.value
        self.left_child = node.left_child
        self.right_child = node.right_child
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def splice_out(self):
        """
        Метод как-бы отсекает узел от дерева
        """
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None

        # Это проверка скорее всего лишняя, т.к. этот метод должен вызываться либо для узла,
        # либо для узла с единственным правым потомком
        elif self.has_right_child():
            if self.is_left_child():
                self.parent.left_child = self.right_child
            else:
                self.parent.right_child = self.right_child
            self.right_child.parent = self.parent

    def find_min(self) -> "TreeNode":
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def next(self) -> "TreeNode":
        if self.has_right_child():
            return self.right_child.find_min()
        else:
            return self.right_ancestor()

    def right_ancestor(self) -> "TreeNode":
        if not self.parent:
            return self

        if self.key < self.parent.key:
            return self.parent
        else:
            return self.parent.right_ancestor()


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    @staticmethod
    def create_node(key, value, parent=None):
        return TreeNode(key, value, parent=parent)

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = self.create_node(key, value)
        self.size += 1

    def _put(self, key, value, current_node):
        if current_node.key < key:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = self.create_node(key, value, current_node)
        elif current_node.key > key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = self.create_node(key, value, current_node)
        else:
            current_node.value = value

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        res = self._get(key, self.root)
        return res.value if res else None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        """
        общий метод удаления ключа из дерева
        """
        node_to_remove = self._get(key, self.root)
        if node_to_remove:
            self.remove(node_to_remove)
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, current_node):
        """
        метод, который непосредственно удаляет ключ из дерева
        """
        if current_node.is_leaf():
            if current_node.is_left_child():
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():
            successor = current_node.right_child.find_min()
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
        else:
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    # Это означает, что current_node - корень.
                    current_node.replace_node_data(current_node.left_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    # Это означает, что current_node - корень.
                    current_node.replace_node_data(current_node.right_child)

    def __delitem__(self, key):
        self.delete(key)

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node: TreeNode, key):
        if node.key == key:
            return node

        if node.key > key:
            if node.has_left_child():
                node = self._find(node.left_child, key)
        else:
            if node.has_right_child():
                node = self._find(node.right_child, key)

        return node

    def range_search(self, left, right):
        result = []
        node = self.find(left)
        while node.key <= right:
            if node.key >= left:
                result.append(node)
            node = node.next()
        return result

    @classmethod
    def merge_with_root(cls, tree_one_root, tree_two_root, root) -> 'BinarySearchTree':
        root.left_child = tree_one_root
        root.right_child = tree_two_root
        tree_one_root.parent = root
        tree_two_root.parent = root
        return cls(root=root)

    @classmethod
    def merge(cls, tree_one, tree_two) -> 'BinarySearchTree':
        """
        Input: tree_one and tree_two with all keys in tree_one's tree smaller than those in tree_two's
        Output: The root of a new tree with all the elements of both trees
        """
        import math

        node = tree_one.find(math.inf)
        tree_one.delete(node.key)
        return cls.merge_with_root(tree_one.root, tree_two.root, node)

    def get_depth(self):
        return self._get_depth(self.root)

    def _get_depth(self, root):
        if root is None:
            return 0
        v1 = self._get_depth(root.left_child)
        v2 = self._get_depth(root.right_child)
        return max(v1, v2) + 1

    def get_size(self):
        return self._get_size(self.root)

    def _get_size(self, root):
        if root is None:
            return 0

        return 1 + self._get_size(root.left_child) + self._get_size(root.right_child)

    def print_yourself(self):
        current_level = [self.root]
        cl = 1
        depth = self.get_depth()
        line_length = (2**depth)*2 - 3
        while current_level:
            # print(current_level)
            indentation = 2**((depth - cl) + 1) - 2
            count_elements = 2 ** (cl - 1)
            indentation_el = int(
                ((line_length - 2*indentation) - count_elements) / (count_elements-1 if count_elements-1 else 1)
            )

            print(' '*indentation, end='')
            for node in current_level:
                if hasattr(node, 'key'):
                    print('{}{}'.format(node.key, ' '*indentation_el), end='')
                else:
                    print('{}{}'.format(node, ' '*indentation_el), end='')
            print()

            next_level = list()
            cause = all([not isinstance(n, TreeNode) for n in current_level])
            for n in current_level:
                if cause:
                    break
                next_level.append(n.left_child if n != '-' and n.has_left_child() else '-')
                next_level.append(n.right_child if n != '-' and n.has_right_child() else '-')

            current_level = next_level
            cl += 1

    def level_traversal(self):
        if self.root is None:
            return

        array = [self.root]
        while array:
            node = array.pop(0)
            print(node.key, end=" ")
            if node.left_child:
                array.append(node.left_child)
            if node.right_child:
                array.append(node.right_child)

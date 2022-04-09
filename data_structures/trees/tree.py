import operator
from data_structures.stack import Stack


class TreesCounter:
    def __init__(self):
        self.cache = {}

    def count(self, vertex_number):
        if vertex_number > 0:
            sum = 0
            for i in range(vertex_number):
                if i in self.cache:
                    v1 = self.cache[i]
                else:
                    v1 = self.count(i)
                    self.cache[i] = v1

                if vertex_number - i - 1 in self.cache:
                    v2 = self.cache[vertex_number - i - 1]
                else:
                    v2 = self.count(vertex_number - i - 1)
                    self.cache[vertex_number - i - 1] = v2

                sum += v1*v2
            return sum

        else:
            return 1


class BinaryTree:
    def __init__(self, root_value):
        self.key = root_value
        self.left_child = None
        self.right_child = None

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_root_val(self):
        return self.key

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            tmp = BinaryTree(value)
            tmp.left_child = self.left_child
            self.left_child = tmp

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            tmp = BinaryTree(value)
            tmp.right_child = self.right_child
            self.right_child = tmp

    def set_root_val(self, value):
        self.key = value

    @classmethod
    def build_parse_tree(cls, fpexp):
        p_stack = Stack()
        e_tree = cls('')
        p_stack.push(e_tree)
        current_tree = e_tree
        for i in fpexp.split():
            if i == '(':
                current_tree.insert_left('')
                p_stack.push(current_tree)
                current_tree = current_tree.get_left_child()
            elif i.isdigit():
                current_tree.set_root_val(int(i))
                current_tree = p_stack.pop()
            elif i in ['+', '-', '*', '/']:
                current_tree.set_root_val(i)
                current_tree.insert_right('')
                p_stack.push(current_tree)
                current_tree = current_tree.get_right_child()
            elif i == ')':
                current_tree = p_stack.pop()
            else:
                raise Exception('unknown symbol: ', i)
        return e_tree

    def evaluate(self):
        operator_dict = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        left = self.get_left_child()
        right = self.get_right_child()

        if left and right:
            fn = operator_dict[self.get_root_val()]
            return fn(left.evaluate(), right.evaluate())
        else:
            return self.get_root_val()

    def my_add(self, value):
        root_value = self.get_root_val()
        if value < root_value:
            if self.left_child is None:
                self.left_child = BinaryTree(value)
            else:
                self.left_child.my_add(value)
        else:
            if self.right_child is None:
                self.right_child = BinaryTree(value)
            else:
                self.right_child.my_add(value)

    def get_max_depth(self):
        v1 = self.left_child.get_max_depth() if self.left_child else 0
        v2 = self.right_child.get_max_depth() if self.right_child else 0
        return max(v1, v2) + 1

    def pre_order(self):
        """
        Метод осуществляет обход дерева в прямом порядке
        """
        print(self.key)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def in_order(self, level=0):
        """
        Метод осуществляет симметричный обход дерева
        """
        if self.left_child:
            self.left_child.in_order(level+3)
        print(' '*level, self.get_root_val())
        if self.right_child:
            self.right_child.in_order(level+3)

    def post_order(self):
        """
        Метод осуществляет обход дерева в обратном порядке
        """
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.get_root_val())


if __name__ == '__main__':
    ...

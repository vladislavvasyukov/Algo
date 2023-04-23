class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def __init__(self):
        self.index = 0
    def serialize(self, root):
        if not root:
            return ""

        stack = [root]
        l = []
        while stack:
            t = stack.pop()
            if not t:
                l.append("#")
            else:
                l.append(str(t.val))
                stack.append(t.right)
                stack.append(t.left)

        return ",".join(l)

    def deserialize(self, data):
        if not data:
            return None

        arr = data.split(",")
        return self.helper(arr)

    def helper(self, arr):
        if arr[self.index] == '#':
            return None

        root = TreeNode(val=int(arr[self.index]))
        self.index += 1
        root.left = self.helper(arr)
        self.index += 1
        root.right = self.helper(arr)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)


leaf_5 = TreeNode(val=5)
leaf_11 = TreeNode(val=11)
node_6 = TreeNode(val=6, left=leaf_5, right=leaf_11)
leaf_2 = TreeNode(val=2)
node_7 = TreeNode(val=7, left=leaf_2, right=node_6)


leaf_5_2 = TreeNode(val=5)
node_9 = TreeNode(val=9, left=leaf_5_2)
node_9_2 = TreeNode(val=9, right=node_9)
test_root = TreeNode(val=1, left=node_7, right=node_9_2)


codec = Codec()
codec.inorder(test_root)
print()
ser = codec.serialize(test_root)
print(ser)
new_tree = codec.deserialize(ser)
codec.inorder(new_tree)
print()

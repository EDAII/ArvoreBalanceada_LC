class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1

class Solution:
    def countSmaller(self, nums):
        def height(node):
            return node.height if node else 0
        def size(node):
            return node.size if node else 0
        def update(node):
            node.height = 1 + max(height(node.left), height(node.right))
            node.size = 1 + size(node.left) + size(node.right)
        def rightRotate(y):
            x = y.left
            T2 = x.right
            x.right = y
            y.left = T2
            update(y)
            update(x)
            return x
        def leftRotate(x):
            y = x.right
            T2 = y.left
            y.left = x
            x.right = T2
            update(x)
            update(y)
            return y
        def getBalance(node):
            return height(node.left) - height(node.right) if node else 0

        def insert(node, val):
            if not node:
                return AVLNode(val), 0
            if val <= node.val:
                node.left, count = insert(node.left, val)
            else:
                node.right, count = insert(node.right, val)
                count += size(node.left) + 1 
            update(node)
            balance = getBalance(node)
            if balance > 1:
                if val <= node.left.val:
                    return rightRotate(node), count
                else:
                    node.left = leftRotate(node.left)
                    return rightRotate(node), count
            if balance < -1:
                if val > node.right.val:
                    return leftRotate(node), count
                else:
                    node.right = rightRotate(node.right)
                    return leftRotate(node), count
            return node, count
        res = []
        root = None
        for num in reversed(nums):
            root, cnt = insert(root, num)
            res.append(cnt)
        return res[::-1]

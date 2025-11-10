class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node, vals):
            if not node:
                return
            inorder(node.left, vals)
            vals.append(node.val)
            inorder(node.right, vals)

        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def balance(node):
            if not node:
                return 0
            return height(node.left) - height(node.right)

        def rightRotate(y):
            x = y.left
            T2 = x.right
            x.right = y
            y.left = T2
            return x

        def leftRotate(x):
            y = x.right
            T2 = y.left
            y.left = x
            x.right = T2
            return y


        def avlInsert(root, key):
            if not root:
                return TreeNode(key)
            if key < root.val:
                root.left = avlInsert(root.left, key)
            else:
                root.right = avlInsert(root.right, key)

            balanceamento = balance(root)
            # caso esquerda esquerda
            if balanceamento > 1 and key < root.left.val:
                return rightRotate(root)
            # caso direita direita
            if balanceamento < -1 and key > root.right.val:
                return leftRotate(root)
            # caso esquerda direita
            if balanceamento > 1 and key > root.left.val:
                root.left = leftRotate(root.left)
                return rightRotate(root)
            # caso direita esquerda
            if balanceamento < -1 and key < root.right.val:
                root.right = rightRotate(root.right)
                return leftRotate(root)
            return root

        values = []
        inorder(root, values)
        avlRoot = None
        for val in values:
            avlRoot = avlInsert(avlRoot, val)
        return avlRoot

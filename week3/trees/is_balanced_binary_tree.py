class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def insert(self, val):
        if val < self.val:
            if not self.left:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)

    def __height(self, node):
        if not node:
            return 0

        return 1 + max(self.__height(node.left), self.__height(node.right))

    def height(self):
        return self.__height(self)


def is_balanced(node):
    if not node:
        return True

    if not node.left and not node.right:
        return True

    #return abs(node.left.height()-node.right.height()) <= 1
    return 1 if abs(node.left.height()-node.right.height()) <= 1 else 0


def main():
    """
    root = TreeNode(50)
    root.insert(25)
    root.insert(75)
    root.insert(22)
    root.insert(44)
    root.insert(2)
    #root.insert(4)
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.left.right = TreeNode(5)
    print root.height()
    print root.left.height()
    print root.right.height()
    print is_balanced(root)

if __name__ == "__main__":
    main()

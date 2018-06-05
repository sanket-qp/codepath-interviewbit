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


def inorder(node):
    stack = []
    current = node
    result = []
    while True:
        if current != None:
            stack.append(current)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                result.append(current.val)
                current = current.right 
            else:
                break   
    return result

def main():
    root = TreeNode(50)
    root.insert(25)
    root.insert(75)
    root.insert(22)
    root.insert(44)
    print inorder(root)

if __name__ == "__main__":
    main()

class Tree:
    class Node:
        def __init__(self, val):
            self.left = None
            self.right = None
            self.value = val

        def __str__(self):
            return str(self.val)

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = self.Node(val)
        else:
            traverser = self.root
            while traverser is not None:
                if val > traverser.val:
                    if traverser.right is not None:
                        traverser = traverser.right
                    else:
                        traverser.right = self.Node(val)
                elif traverser.left is not None:
                    traverser = traverser.left
                else:
                    traverser.left = self.Node(val)

    def search(self, val):
        traverser = self.root
        while traverser:
            if val == traverser.val:
                return traverser
            elif val > traverser.val:
                traverser = traverser.right
            else:
                traverser = traverser.left
        return -1  # not found

    # depth first search // stack
    def preorder(self):
        if self.root is None:
            return

    def postorder(self):
        if self.root is None:
            return

    def inorder(self):
        if self.root is None:
            return

    # bredth first search // queue
    def levelorder(self):
        if self.root is None:
            return

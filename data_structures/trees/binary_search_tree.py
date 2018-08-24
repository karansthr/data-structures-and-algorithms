from collections import deque


class Tree:
    class Node:
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = self.Node(value)
        else:
            traverser = self.root
            while traverser:
                if value > traverser.value:
                    if traverser.right:
                        traverser = traverser.right
                    else:
                        traverser.right = self.Node(value)
                        break
                elif traverser.left:
                    traverser = traverser.left
                else:
                    traverser.left = self.Node(value)
                    break

    def search(self, value):
        traverser = self.root
        while traverser:
            if value == traverser.value:
                return traverser
            elif value > traverser.value:
                traverser = traverser.right
            else:
                traverser = traverser.left
        return -1  # not found

    # preorder, inorder and postorder traversal are depth first search
    # so we can implement it with stack, and levelorder traversal is a
    # breadth first search so we can implement that with a queue

    def preorder(self, return_nodes=False):
        if self.root is None:
            yield

        stack = []
        traverser = self.root
        stack.append(traverser)
        while stack:
            traverser = stack.pop()
            if traverser.right:
                stack.append(traverser.right)
            if traverser.left:
                stack.append(traverser.left)
            yield traverser if return_nodes else traverser.value

    def inorder(self, return_nodes=False):
        if self.root is None:
            yield

        traverser = self.root
        stack = [traverser]
        while stack:
            if traverser:
                traverser = traverser.left
            else:
                node = stack.pop()
                yield node if return_nodes else node.value
                traverser = node.right
            if traverser:
                stack.append(traverser)

    def postorder(self, return_nodes=False):
        if self.root is None:
            yield

        stack = []
        if self.root.right:
            stack.append(self.root.right)
        stack.append(self.root)
        traverser = self.root.left
        while stack:
            if not traverser:
                top = stack.pop()
                if stack and top.right == stack[-1]:
                    traverser = stack.pop()
                    stack.append(top)
                else:
                    yield top if return_nodes else top.value
            else:
                if traverser.right:
                    stack.append(traverser.right)
                stack.append(traverser)
                traverser = traverser.left

    # bredth first search // queue
    def levelorder(self, return_nodes=False):
        if self.root is None:
            yield

        traverser = self.root
        queue = deque([traverser])
        while queue:
            traverser = queue.popleft()
            yield traverser if return_nodes else traverser.value
            if traverser.left:
                queue.append(traverser.left)
            if traverser.right:
                queue.append(traverser.right)

    def get_leafs(self, return_nodes=False):
        if self.root is None:
            yield

        traverser = self.root
        stack = [traverser]
        while stack:
            if traverser:
                traverser = traverser.left
                if traverser:
                    stack.append(traverser)
            else:
                traverser = stack.pop()
                if not traverser.right:
                    yield traverser if return_nodes else traverser.value
                else:
                    traverser = traverser.right
                    stack.append(traverser)


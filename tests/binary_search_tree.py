import unittest

from data_structures.trees.binary_search_tree import Tree


class BinarySearchTreeTest(unittest.TestCase):

    def test(self):
        bst = Tree()
        values = [5, 3, 1, 4, 8, 6, 10]
        '''
                 5
               /  \
              3    8
             / \  / \
            1  4 6  10

        '''
        for value in values:
            bst.insert(value)
        self.assertEqual(list(bst.preorder()), [5, 3, 1, 4, 8, 6, 10])
        self.assertEqual(list(bst.postorder()), [1, 4, 3, 6, 10, 8, 5])
        self.assertEqual(list(bst.inorder()), [1, 3, 4, 5, 6, 8, 10])
        self.assertEqual(list(bst.levelorder()), [5, 3, 8, 1, 4, 6, 10])
        self.assertEqual(list(bst.get_leafs()), [1, 4, 6, 10])

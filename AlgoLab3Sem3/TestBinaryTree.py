import unittest
from BinaryTree import BinaryTree
from left_ones import left_ones


class MyTestCase(unittest.TestCase):
    def test_left_ones_1(self):
        root = None
        self.assertEqual(left_ones(root), 0)

    def test_left_ones_2(self):
        root = BinaryTree(5)
        self.assertEqual(left_ones(root), 0)

    def test_left_ones_3(self):
        root = BinaryTree(5)
        root.right = BinaryTree(10)
        root.right.right = BinaryTree(15)
        self.assertEqual(left_ones(root), 0)

    def test_left_ones_4(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)
        root.right.right.left = BinaryTree(10)
        root.right.right.right = BinaryTree(5)
        root.right.left.left = BinaryTree(8)
        root.right.left.right = BinaryTree(13)

        self.assertEqual(left_ones(root), 27)


if __name__ == '__main__':
    unittest.main()

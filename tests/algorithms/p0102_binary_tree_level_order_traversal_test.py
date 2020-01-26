import unittest
from leetcode.algorithms.p0102_binary_tree_level_order_traversal \
    import Solution, TreeNode


class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):
    def test_binary_tree_level_order_traversal(self):
        solution = Solution()
        a = TreeNode(3)
        b = TreeNode(9)
        c = TreeNode(20)
        a.left = b
        a.right = c
        c.left = TreeNode(15)
        c.right = TreeNode(7)
        expected_lists = [
            [3],
            [9, 20],
            [15, 7]
        ]
        actual_lists = solution.levelOrder(a)

        for i in range(len(expected_lists)):
            self.assertListEqual(expected_lists[i], actual_lists[i])

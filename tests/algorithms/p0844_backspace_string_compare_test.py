import unittest
from leetcode.algorithms.p0844_backspace_string_compare import Solution


class TestBackspaceStringCompare(unittest.TestCase):
    def test_backspace_string_compare(self):
        solution = Solution()

        self.assertTrue(solution.backspaceCompare('ab#c', 'ad#c'))
        self.assertFalse(solution.backspaceCompare('a#c', 'b'))

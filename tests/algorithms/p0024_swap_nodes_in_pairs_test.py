import unittest
from leetcode.algorithms.p0024_swap_nodes_in_pairs \
    import Solution, ListNode
from .list_helper import convert_linked_list_to_list


class TestSwapNodesInPairs(unittest.TestCase):
    def test_swap_nodes_in_pairs(self):
        solution = Solution()
        a = ListNode(1)
        b = ListNode(2)
        c = ListNode(3)
        d = ListNode(4)
        c.next = d
        b.next = c
        a.next = b

        self.assertListEqual(
            [2, 1, 4, 3], convert_linked_list_to_list(solution.swapPairs(a)))

import unittest
from leetcode.algorithms.p0170_two_sum_iii_1 import TwoSum as TwoSum1
from leetcode.algorithms.p0170_two_sum_iii_2 import TwoSum as TwoSum2


class TestTwoSum(unittest.TestCase):
    def test_two_sum1(self):
        two_sum = TwoSum1()
        two_sum.add(1)
        two_sum.add(3)
        two_sum.add(5)

        self.assertTrue(two_sum.find(4))
        self.assertFalse(two_sum.find(7))

    def test_two_sum2(self):
        two_sum = TwoSum2()
        two_sum.add(1)
        two_sum.add(3)
        two_sum.add(5)

        self.assertTrue(two_sum.find(4))
        self.assertFalse(two_sum.find(7))

import unittest

from algorithms.dynamic_programming import (
        kadane_algorithm,
        ways_to_reach_nth_step,
        fibonacci
    )


class dptest(unittest.TestCase):
    def test_max_subarray_sum(self):
        self.assertEqual(kadane_algorithm.max_subarray([5, 3, -10, 6, 3, -3, 1]), 9)

    def test_ways_to_reach_nth_step(self):
        self.assertEqual(ways_to_reach_nth_step.count_ways(3), 3)
        self.assertEqual(ways_to_reach_nth_step.count_ways(4), 5)
        self.assertEqual(ways_to_reach_nth_step.count_ways(5), 8)
        self.assertEqual(ways_to_reach_nth_step.count_ways(6), 13)

    def test_fibonacci(self):
        self.assertRaises(Exception, fibonacci.fibonacci, 0)
        self.assertEqual(fibonacci.fibonacci(1), 1)
        self.assertEqual(fibonacci.fibonacci(2), 1)
        self.assertEqual(fibonacci.fibonacci(3), 2)
        self.assertEqual(fibonacci.fibonacci(4), 3)
        self.assertEqual(fibonacci.fibonacci(5), 5)
        self.assertEqual(fibonacci.fibonacci(7), 13)
        self.assertEqual(fibonacci.fibonacci(15), 610)
        self.assertEqual(fibonacci.fibonacci(67), 44945570212853)

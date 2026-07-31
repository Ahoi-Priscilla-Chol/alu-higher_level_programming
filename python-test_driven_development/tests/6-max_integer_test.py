#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_ordered_list(self):
        """Max of an already ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max of an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Max of a descending list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_start(self):
        """Max value is the first element"""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        """Max value is the last element"""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_single_element(self):
        """List with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument uses the default empty list"""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """List of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        """List with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-10, 0, 5, -3, 8]), 8)

    def test_duplicate_max_values(self):
        """List with duplicate max values"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        """List of floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)


if __name__ == '__main__':
    unittest.main()

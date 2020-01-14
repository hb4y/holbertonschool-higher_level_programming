#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Testing class
    """
    def test_max(self):
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([-1, -2]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([5, 3, 1]), 5)
        self.assertEqual(max_integer([1, 3, 2]), 5)

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Suite test for max_integer function"""

    def test_max_integer(self):
        self.assertEqual(max_integer([10, -4, 120, 3]), 120)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_repeated_number(self):
        self.assertEqual(max_integer([100, 100, 100]), 100)

    def test_float_numbers(self):
        self.assertEqual(max_integer([500, 510, 500, 490]), 510)

    def test_max_operated_integer(self):
        self.assertEqual(max_integer([-4, -5 * -5, 22, -1]), 25)

    def test_neg_numbers(self):
        self.assertEqual(max_integer([-10, -6, -3, -1]), -1)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([15, 14, 13, 12, 11]), 15)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_big_list(self):
        self.assertEqual(max_integer([
            901, 902, 903, 9004, 9005, 9060, 907, 908, 909, 910,
            911, 912, 913, 914, 915, 9160, 917, 918, 919, 920,
            9109, 9018, 9170, 10000, 9015, 914, 913, 912, 911, 910,
            9009, 9008, 9070, 9060, 9050, 9040, 9030, 9020, 9010]), 10000)

    def test_list_with_loop(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def test_one_number_in_a_list(self):
        self.assertEqual(max_integer([10]), 10)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, '10'])

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([100, (200, 300)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 10, 'key2': 20})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(10)

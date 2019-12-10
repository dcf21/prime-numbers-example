#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit tests for the PrimeNumber search class
"""

import unittest
from prime_numbers import PrimeNumbers


class TestPrimeNumbers(unittest.TestCase):

    def test_out_of_range_error(self):
        with self.assertRaises(ValueError):
            PrimeNumbers.test_if_prime(value=-1)

    def test_1_is_prime(self):
        self.assertEqual(PrimeNumbers.test_if_prime(value=1), False)

    def test_2_is_prime(self):
        self.assertEqual(PrimeNumbers.test_if_prime(value=2), True)

    def test_4_is_prime(self):
        self.assertEqual(PrimeNumbers.test_if_prime(value=4), False)


# Run tests if we are run from command line
if __name__ == '__main__':
    unittest.main()

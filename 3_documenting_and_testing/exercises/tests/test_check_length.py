#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Mohammed Elfadil
"""
import unittest

from ..check_length import check_length

class TestCheckLength(unittest.TestCase):
    """Test the check_length function"""
    
    def test_integers(self):
        """It should evaluate [1, 2, 3, 4, 5] to 5"""
        actual = check_length([1, 2, 3, 4, 5]) # call function with test arguments
        expected = 5 # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_0(self):
        """It should evaluate [] to 0"""
        actual = check_length([])
        expected = None
        self.assertEqual(actual, expected)

    def test_str(self):
        """It should evaluate ["a", "b", "c"] to 3"""
        actual = check_length(["a", "b", "c"])
        expected = 3
        self.assertEqual(actual, expected)

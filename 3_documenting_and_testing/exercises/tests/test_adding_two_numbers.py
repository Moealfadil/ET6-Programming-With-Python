#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Mohammed Elfadil
"""
import unittest

from ..adding_two_numbers import adding_two_numbers

class Testaddingtwonumbers(unittest.TestCase):
    """test the adding_two_numbers function"""
    def test_1(self):
        """It should evaluate 1,2 to 3"""
        actual = adding_two_numbers(1,2)
        expected = 3
        self.assertEqual(actual,expected)
    def test_2(self):
        """It should evaluate 3,4 to 7"""
        actual = adding_two_numbers(3,4)
        expected = 7
        self.assertEqual(actual,expected)
    def test_str_to_int(self):
        """It should evaluate "7",6 to AssertionError"""
        with self.assertRaises(AssertionError):
            adding_two_numbers("7",6)
    def test_4(self):
        """its should evaluate 7,6 to 13"""
        actual = adding_two_numbers(7,6)
        expected = 13
        self.assertEqual(actual,expected)
    def test_addingzeros(self):
        """It should evaluate 0,0 to 0"""
        actual = adding_two_numbers(0,0)
        expected = 0
        self.assertEqual(actual,expected)

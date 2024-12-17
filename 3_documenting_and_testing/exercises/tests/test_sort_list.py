#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Mohammed Elfadil
"""
import unittest

from ..sort_list import sort_list

class TestSortList(unittest.TestCase):
    """ Test the sort_list function """
    
    def test_desending_numbers(self):
        """ It should evaluate [3, 2, 1] to [1, 2, 3] """
        actual = sort_list([3, 2, 1])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_random(self):
        """ It should evaluate [3, 2, 1, 4, 5] to [1, 2, 3, 4, 5] """
        actual = sort_list([3, 2, 1, 4, 5])
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(actual, expected)

    def test_sorted(self):
        """ It should evaluate [1, 2, 3] to [1, 2, 3] """
        actual = sort_list([1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        """ It should evaluate [] to [] """
        actual = sort_list([])
        expected = []
        self.assertEqual(actual, expected)

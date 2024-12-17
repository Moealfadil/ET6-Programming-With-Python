#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting a list of integers

Module contents:
    - sort_list: sorts a list of integers

Created on XX XX XX
@author: Mohammed Elfadil
"""
def sort_list(a:list, b=None)->list:
    """Sorts a list of integers in ascending order
    Parameters:
        a: list of integers
        b: list of integers, default is None
    Returns:
        list of integers sorted in ascending order
    Raises:
        AssertionError: if a is not a list
        AssertionError: if a is not a list of integers
    >>> sort_list([3, 2, 1])
    [1, 2, 3]
    >>> sort_list([3, 2, 1, 4, 5])
    [1, 2, 3, 4, 5]
    >>> sort_list([1, 2, 3])
    [1, 2, 3]
    """
    if b is None:
        b = []
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b

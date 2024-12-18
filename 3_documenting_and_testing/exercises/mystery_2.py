#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking length of a list

Module contents:
    - check_length: checks the length of a list

Created on XX XX XX
@author: Mohammed Elfadil
"""
def check_length(a:list) -> int:
    """Checks the length of a list
    Parameters:
        a: list, a list of any type
    Returns -> int, the length of the list
    Raises:
        AssertionError: if the argument is not a list
    >>> check_length([1, 2, 3, 4, 5])
    5
    >>> check_length([])
    0
    >>> check_length(["a", "b", "c"])
    3
    """
    if len(a) == 0:
        return None

    return len(a)

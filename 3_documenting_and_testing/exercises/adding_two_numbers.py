#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for adding two numbers together.

Module contents:
    - adding_two_numbers: adds two numbers together.

Created on XX XX XX
@author: Mohammed Elfadil
"""
def adding_two_numbers(a: int,b:int) -> int:
    """Adds two numbers together.
    Parameter:
        a: int
        b: int
    Return -> int:sum of a and b
    Raises:
        AssertionError: if the argument is not an integer
    >>> adding_two_numbers(1,2)
    3
    >>> adding_two_numbers(3,4)
    7
  >>> adding_two_numbers("7",6)
  Traceback (most recent call last):
    ...
    AssertionError: a is not an integer
  """
    return a + b

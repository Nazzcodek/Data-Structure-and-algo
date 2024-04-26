#!/usr/bin/env python
"""
This module contains a function is_leap that determines if a given year is a leap year
Args:
    year: int
Returns:
    True if year is a leap year
    False if year is not a leap year
"""
def is_leap(year):
    """This function returns true if year is a leap year"""
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap
    
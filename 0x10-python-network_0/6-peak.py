#!/usr/bin/python3
""" This script finds a peak within a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Args:
        list_of_integers (list): List of integers to identify a peak from.
    Returns:
        int or None: Returns the peak of the list_of_integers, or None if list is empty.
    """
    size = len(list_of_integers)
    mid_e = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        mid_e = mid_e // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid + mid_e // 2
        elif mid_e > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid - mid_e // 2
        else:
            return list_of_integers[mid]

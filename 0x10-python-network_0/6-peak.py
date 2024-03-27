#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: A peak value from the list.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            # Move right if the peak is on the right side
            left = mid + 1
        else:
            # Move left if the peak is on the left side or at mid
            right = mid

    # At the end of the loop, left and right will converge to a peak
    return list_of_integers[left]

# Example usage:
# list_of_integers = [1, 3, 20, 4, 1, 0]
# peak_value = find_peak(list_of_integers)
# print("Peak value:", peak_value)

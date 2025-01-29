"""
Python Array and List Programming Exercises
----------------------------------------
This file contains 30 programming exercises focusing on array and list manipulation,
from basic to advanced level. Each function has a description and test cases.

Instructions:
1. Implement each function according to its description
2. Run the test cases to verify your implementation
3. Try to solve without using built-in functions first to understand the logic
"""

def reverse_list(arr):
    """
    Basic: Reverse a list without using built-in functions
    Args: arr (list): Input list
    Returns: list: Reversed list
    """
    print(arr[::-1])
    return arr[::-1]
    pass

def find_second_largest(arr):
    """
    Basic: Find the second largest element in a list
    Args: arr (list): Input list of numbers
    Returns: number: Second largest element or None if not found
    """

    arr.sort()
    return arr[-2]
    pass

def remove_duplicates(arr):
    """
    Basic: Remove duplicates from a list while maintaining order
    Args: arr (list): Input list
    Returns: list: List with duplicates removed
    """

    arr = list(set(arr))
    return arr
    pass

def rotate_list(arr, k):
    """
    Basic: Rotate list to the right by k steps
    Args: 
        arr (list): Input list
        k (int): Number of steps to rotate
    Returns: list: Rotated list
    """

    from collections import deque

    queue = deque(arr)
    queue.rotate(k)

    return list(queue)

    pass

def merge_sorted_lists(arr1, arr2):
    """
    Basic: Merge two sorted lists into a single sorted list
    Args:
        arr1 (list): First sorted list
        arr2 (list): Second sorted list
    Returns: list: Merged sorted list
    """

    i = j = k = 0
    new_array = [0] * (len(arr1) + len(arr2))

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            new_array[k] = arr1[i]
            i += 1
        else:
            new_array[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        new_array[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        new_array[k] = arr2[j]
        j += 1
        k += 1

    return new_array



def find_missing_number(arr):
    """
    Basic: Find missing number in array containing 1 to n
    Args: arr (list): List of numbers from 1 to n with one missing
    Returns: int: The missing number
    """
    pass

def move_zeros_to_end(arr):
    """
    Basic: Move all zeros to end of array maintaining relative order
    Args: arr (list): Input list
    Returns: list: List with zeros at end
    """
    pass

def find_pairs_with_sum(arr, target):
    """
    Basic: Find all pairs in array that sum to target
    Args:
        arr (list): Input list
        target (int): Target sum
    Returns: list of tuples: Pairs that sum to target
    """
    pass

def intersection_of_arrays(arr1, arr2):
    """
    Basic: Find intersection of two arrays
    Args:
        arr1 (list): First array
        arr2 (list): Second array
    Returns: list: Common elements
    """
    pass

def is_palindrome_list(arr):
    """
    Basic: Check if list is palindrome
    Args: arr (list): Input list
    Returns: bool: True if palindrome, False otherwise
    """
    pass

def find_peak_element(arr):
    """
    Intermediate: Find a peak element (element greater than neighbors)
    Args: arr (list): Input list
    Returns: int: Index of peak element
    """
    pass

def max_subarray_sum(arr):
    """
    Intermediate: Find maximum sum of contiguous subarray
    Args: arr (list): Input list of numbers
    Returns: int: Maximum sum
    """
    pass

def dutch_flag_sort(arr):
    """
    Intermediate: Sort array of 0s, 1s, and 2s in-place
    Args: arr (list): Input list containing only 0s, 1s, and 2s
    Returns: list: Sorted array
    """
    pass

def find_majority_element(arr):
    """
    Intermediate: Find element appearing more than n/2 times
    Args: arr (list): Input list
    Returns: Element that appears more than n/2 times, or None
    """
    pass

def trap_rain_water(heights):
    """
    Intermediate: Calculate water that can be trapped between bars
    Args: heights (list): List of bar heights
    Returns: int: Units of water trapped
    """
    pass

def longest_consecutive_sequence(arr):
    """
    Intermediate: Find length of longest consecutive sequence
    Args: arr (list): Input list of numbers
    Returns: int: Length of longest consecutive sequence
    """
    pass

def circular_array_loop(arr):
    """
    Intermediate: Detect if array has a circular loop
    Args: arr (list): Input list of numbers
    Returns: bool: True if circular loop exists, False otherwise
    """
    pass

def min_platforms_needed(arrivals, departures):
    """
    Intermediate: Find minimum platforms needed for railway station
    Args:
        arrivals (list): Train arrival times
        departures (list): Train departure times
    Returns: int: Minimum platforms needed
    """
    pass

def next_permutation(arr):
    """
    Intermediate: Find next lexicographically greater permutation
    Args: arr (list): Input list
    Returns: list: Next permutation
    """
    pass

def jump_game(arr):
    """
    Intermediate: Determine if can reach last index
    Args: arr (list): List where each element represents max jump length
    Returns: bool: True if can reach end, False otherwise
    """
    pass

def find_duplicates_space_efficient(arr):
    """
    Advanced: Find all duplicates in array using O(1) extra space
    Args: arr (list): Input list where elements are in range [1, n]
    Returns: list: List of duplicates
    """
    pass

def longest_mountain(arr):
    """
    Advanced: Find length of longest mountain subarray
    Args: arr (list): Input list
    Returns: int: Length of longest mountain
    """
    pass

def smallest_range_covering_elements(lists):
    """
    Advanced: Find smallest range that includes at least one number from each list
    Args: lists (list of lists): K sorted lists
    Returns: tuple: (start, end) of smallest range
    """
    pass

def max_chunks_to_sorted(arr):
    """
    Advanced: Maximum number of chunks array can be split into to become sorted
    Args: arr (list): Input list of numbers 0 to n-1
    Returns: int: Maximum number of chunks
    """
    pass

def sliding_window_maximum(arr, k):
    """
    Advanced: Find maximum element in sliding window
    Args:
        arr (list): Input list
        k (int): Window size
    Returns: list: Maximum elements for each window
    """
    pass

def min_swaps_to_sort(arr):
    """
    Advanced: Find minimum swaps required to sort array
    Args: arr (list): Input list
    Returns: int: Minimum number of swaps
    """
    pass

def longest_subarray_with_sum_k(arr, k):
    """
    Advanced: Find length of longest subarray with sum k
    Args:
        arr (list): Input list
        k (int): Target sum
    Returns: int: Length of longest subarray
    """
    pass

def min_operations_to_palindrome(arr):
    """
    Advanced: Minimum operations to make array palindrome
    Args: arr (list): Input list
    Returns: int: Minimum number of operations
    """
    pass

def find_original_array(changed):
    """
    Advanced: Find original array from doubled array
    Args: changed (list): Array where each element is doubled
    Returns: list: Original array or empty if impossible
    """
    pass

def max_rect_histogram(heights):
    """
    Advanced: Find largest rectangle area in histogram
    Args: heights (list): List of bar heights
    Returns: int: Area of largest rectangle
    """
    pass

# Test cases
def run_tests():
    # Basic Tests
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert find_second_largest([1, 5, 3, 2, 4]) == 4
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert find_missing_number([1, 2, 4, 5]) == 3
    assert move_zeros_to_end([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert find_pairs_with_sum([1, 2, 3, 4, 5], 7) == [(2, 5), (3, 4)]
    assert intersection_of_arrays([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert is_palindrome_list([1, 2, 2, 1]) == True

    # Intermediate Tests
    assert find_peak_element([1, 3, 20, 4, 1, 0]) == 2
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert dutch_flag_sort([2, 0, 1, 1, 0, 2]) == [0, 0, 1, 1, 2, 2]
    assert find_majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
    assert trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4
    assert circular_array_loop([2, -1, 1, 2, 2]) == True
    assert min_platforms_needed([900, 940], [910, 1200]) == 2
    assert next_permutation([1, 2, 3]) == [1, 3, 2]
    assert jump_game([2, 3, 1, 1, 4]) == True

    # Advanced Tests
    assert find_duplicates_space_efficient([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
    assert longest_mountain([2, 1, 4, 7, 3, 2, 5]) == 5
    assert smallest_range_covering_elements([[4, 10, 15], [24, 25], [2, 3, 20]]) == (3, 24)
    assert max_chunks_to_sorted([1, 0, 2, 3, 4]) == 4
    assert sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert min_swaps_to_sort([4, 3, 2, 1]) == 2
    assert longest_subarray_with_sum_k([10, 5, 2, 7, 1, 9], 15) == 4
    assert min_operations_to_palindrome([1, 4, 5, 9, 1]) == 1
    assert find_original_array([1, 3, 2, 4]) == [1, 2]
    assert max_rect_histogram([2, 1, 5, 6, 2, 3]) == 10

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
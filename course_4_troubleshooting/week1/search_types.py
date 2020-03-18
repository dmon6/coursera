#!/usr/bin/env python3.7
def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1


def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1


test_list = [x for x in range(1, 100001)]
test_find = 10000
test_case = linear_search(test_list, test_find)
#test_case2 = binary_search(test_list, test_find)

print(f'Found test_find: {test_find} at index {test_case}')
#print(f'Found test_find: {test_find} at index {test_case2}')

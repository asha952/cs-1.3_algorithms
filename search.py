#!python

def linear_search(array, item):
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    for index, value in enumerate(array):
        if item == value:
            return index  # Found
    return None  # Not found


def linear_search_recursive(array, item, index=0):
    if index > len(array) - 1:
        return None
    if item == array[index]:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array) - 1

    while right >= left:
        middle = (right + left) // 2
        if item > array[middle]:  # Shift the left if item is greater than middle of array
            left = middle + 1
        elif item < array[middle]:
            right = middle - 1
        else:
            return middle

    return None


def binary_search_recursive(array, item, left=None, right=None):
    if left == None:
        left = 0
        right = len(array) - 1

    middle = (left + right) // 2

    if right < left:
        return None
    elif array[middle] == item:
        return middle

    if array[middle] < item:
        return binary_search_recursive(array, item, left=middle + 1, right=right)
    else:
        return binary_search_recursive(array, item, left=left, right=middle - 1)

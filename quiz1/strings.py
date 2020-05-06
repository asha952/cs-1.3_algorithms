#!python


def contains_recursively(text_arr, pattern_arr):
    pattern_index = 0
    if len(pattern_arr) > len(text_arr):
        return False
    for i in range(len(text_arr)):
        if text_arr[i] != pattern_arr[pattern_index]:
            pattern_index = 0
        if text_arr[i] == pattern_arr[pattern_index]:
            pattern_index += 1
            if pattern_index == len(pattern_arr):
                return True
    return False


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    text_arr = "".join(c.lower() for c in text if c.isalpha())
    pattern_arr = "".join(c.lower() for c in pattern if c.isalpha())
    if len(pattern_arr) == 0:  # handle if pattern_arr is empty, then return true
        return True
    return contains_recursively(text_arr, pattern_arr)


def find_index_recursively(text_arr, pattern_arr):
    pattern_index = 0
    for i in range(len(text_arr)):
        if text_arr[i] != pattern_arr[pattern_index]:
            pattern_index = 0
        if text_arr[i] == pattern_arr[pattern_index]:
            pattern_index += 1
            if pattern_index == len(pattern_arr):
                return i + 1 - pattern_index
    return None


def find_index(text, pattern):
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    text_arr = "".join(c.lower() for c in text if c.isalpha() or c.isspace())
    pattern_arr = "".join(c.lower() for c in pattern if c.isalpha() or c.isspace())
    if len(pattern_arr) == 0:
        return 0
    
   
    index = find_index_recursively(text_arr, pattern_arr)
    return index


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()

import string


# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text)


# def is_palindrome_recursive(text, left=None, right=None):
#     # once implemented, change is_palindrome to call is_palindrome_recursive
#     # to verify that your iterative implementation passes all tests
#     text_array = "".join(c.lower() for c in text if c.isalpha())
#     half = int(len(text_array) // 2 + (len(text_array) % 2 > 0))
#     if left == None:
#         left = 0
#     if right == None:
#         right = len(text_array) - 1

#     if left < half:
#         if text_array[left] == text_array[right]:
#             return is_palindrome_recursive(text, left+1, right-1)
#         else:
#             return False
#     else:
#         return True

# def is_palindrome_iterative(text):
#     pass
#     # once implemented, change is_palindrome to call is_palindrome_iterative
#     # to verify that your iterative implementation passes all tests
#     text_array = "".join(c.lower() for c in text if c.isalpha())
#     half = int(len(text_array) // 2 + (len(text_array) % 2 > 0))
#     for index in range(half): #loop until halfway
#         if text_array[index] != text_array[len(text_array) - 1 - index]:
#             return False
#     return True


def is_palindrome_iterative(text):
    text_array = "".join(c.lower() for c in text if
                         c.isalpha())
    half = int(len(text_array) // 2 + (len(
        text_array) % 2 > 0))
    for index in range(half):
        if text_array[index] != text_array[len(text_array) - 1 - index]:
            return False
    return True


def is_palindrome_recursive(text, left=None, right=None):
    text_array = "".join(c.lower() for c in text if c.isalpha())
    half = int(len(text_array) // 2 + (len(text_array) % 2 > 0))
    if left is None:
        left = 0
    if right is None:
        right = len(text_array) - 1

    if left < half:
        if text_array[left] == text_array[right]:
            return is_palindrome_recursive(text, left + 1, right - 1)
        else:
            return False
    else:
        return True


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()

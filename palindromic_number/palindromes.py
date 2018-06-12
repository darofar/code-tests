"""
PROBLEM
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

ANALYSIS
Multiplying two N-digit numbers yields a number with a length of 2N or 2N-1.
Assuming that after multiplying these numbers we can always obtain at least a
palindrome of the greater length (2N) the search can be reduced to find the
greater palindrome of length 2N.
"""


def reversed_string(a_string):
    return a_string[::-1]


def is_palindrome(number):
    """
    Returns true if the number is palindromic
    """
    number_str = str(number)
    middle_point = int(len(number_str)/2)
    if number_str[:middle_point] == reversed_string(number_str[-middle_point:]):
        return True
    return False


def get_largest_palindrome_for_digits(digits):
    """
    Returns the largest palindromic number for multiply two numbers of same digit size
    """
    max_top = int("9"*digits)
    min_top = int("9"*(digits-1)) if digits > 1 else 0
    min_digits = digits*2
    max_found = None
    for digit_A in range(max_top, min_top, -1):
        result = None
        for digit_B in range(max_top, min_top, -1):
            result = digit_A*digit_B
            if len(str(result)) < min_digits:
                break
            if is_palindrome(result):
                if not max_found or max_found[2] < result:
                    max_found = [digit_A, digit_B, result]
            elif digit_A == digit_B:
                break
        if len(str(result)) < min_digits:
            break
    print("Largest palindromic number is: " + str(max_found[2]))
    print("As a result of multiply the digits: " + str(max_found[0]) + "x" + str(max_found[1]))


if "__main__" in __name__:
    get_largest_palindrome_for_digits(3)

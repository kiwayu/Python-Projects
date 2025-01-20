
def is_palindrome(values: str) -> bool:
    """Determine if a string is a numerical palindrome.

    The function checks if the length of the input is greater than 1
    and has no leading zeros.
    Additionally, checks that the string is numerical.
    Iterate over the first half of the list, ascertained using floor division
    compare the value to the corresponding value moving down from the end
    of the list.
    If the values do not match. Return False.
    If the values match. Return True
    """
    if len(values) <= 1 or values[0] == '0' and len(values) > 1:
        return False
    if set(values) - set("0123456789"):
        return False
    for i in range(0, (len(values) // 2)):
        if (values[i] != values[len(values) - i - 1 ]):
            return False
    return True

print(is_palindrome("1221"))    # Even palindrome - expected: True
print(is_palindrome("10201"))   # Odd palindrome - expected: True
print(is_palindrome("010"))     # Palindrome with leading zero - expected: False
print(is_palindrome("011"))     # Leading zero - expected: False
print(is_palindrome("a1221"))   # Letter character - expected: False
print(is_palindrome("12.21"))   # Non-numeric character - expected: False

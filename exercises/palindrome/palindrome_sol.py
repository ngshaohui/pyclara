"""
A palindrome is a string which is read the same forwards and backwards

Write a program that checks if a string is a palindrome

The input string is guaranteed to be made of a single word, entirely in lowercase characters, and contain at least 1 character.

Examples

If the string is "abba"
The string is a palindrome

If the string is "no"
The string is not a palindrome

If the string is "cisabbasic"
The string is a palindrome
"""


def is_palindrome(st: str) -> bool:
    "check if string is a palindrome"
    # start pointing at opposite ends of the string
    start = 0
    end = len(st) - 1
    while start < end:
        if st[start] != st[end]:
            return False
        # move pointers one position towards middle
        start += 1
        end -= 1
    return True


def is_palindrome2(st: str) -> bool:
    "check if string is a palindrome"
    # reversed gives us an iterator object, so we need to convert it to a string before using it
    return st == "".join(reversed(st))


def main():
    print(is_palindrome("abba"))


if __name__ == "__main__":
    main()

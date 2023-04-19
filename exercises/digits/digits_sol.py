"""
Write a program that calculates the sum of the digits in a non-negative number

Example

If the number given is 1933091
the sum is 1 + 9 + 3 + 3 + 0 + 9 + 1 = 26

If the number given is 0
the sum is 0
"""


def sum_digits(digits: int) -> int:
    "calculate sum of all individual digits in a number"
    digits_sum = 0
    # convert number to a collection of characters
    digits_str = str(digits)
    for digit_str in digits_str:
        # convert each character to an integer
        digit = int(digit_str)
        digits_sum += digit
    return digits_sum


def sum_digits2(digits: int) -> int:
    "calculate sum of all individual digits in a number"
    digits_sum = 0
    # sum digits from back to front
    while digits > 0:
        # get last digit in the number
        last_digit = digits % 10
        digits_sum += last_digit
        # truncate last digit in the number
        digits = digits // 10
    return digits_sum


def sum_digits3(digits: int) -> int:
    "calculate sum of all individual digits in a number"
    # convert number to a collection of characters
    digits_str = str(digits)
    # convert each digit character to an array of numbers
    num_arr = map(int, digits_str)
    return sum(num_arr)


def main():
    print(sum_digits(1933091))


if __name__ == "__main__":
    main()

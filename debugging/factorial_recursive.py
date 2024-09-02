#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer.

    Description:
    This function computes the factorial of a non-negative integer `n` using
    recursion. The factorial of `n`, denoted as `n!`, is the product of all
    positive integers less than or equal to `n`. For example, factorial(5) is
    5 * 4 * 3 * 2 * 1 = 120. By definition, factorial(0) is 1.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input integer `n`. If `n` is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Check if an argument is provided via command line
if len(sys.argv) != 2:
    print("Usage: python script.py <non-negative integer>")
    sys.exit(1)

# Parse the argument and compute factorial
try:
    number = int(sys.argv[1])
    if number < 0:
        raise ValueError("The number must be a non-negative integer.")
except ValueError as e:
    print(e)
    sys.exit(1)

# Compute factorial and print result
f = factorial(number)
print(f)

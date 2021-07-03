"""
Prints the number of calls of a recursive Fibonacci function with problem sizes that double.
"""

from random import randint
from collections import Counter

def fib(n, counter):
    """Count the number of calls of the Fibonacci function."""
    if n < 3:
        return 1
    else:
        return fib(n - 1, counter) + fib(n - 2, counter)

print(fib(10, 45))
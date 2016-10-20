"""
Problem:

    The fibonacci numbers start 1, 1, 2, 3, 5, 8, 13, ...
    The next number in each sequence is given by adding the last
    two terms.

    The function fib takes an integer n and should return the
    nth fibonacci number

Tests:

    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(5)
    5
    >>> fib(10)
    55

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def fib(n):
    fib1 = 0
    fib2 = 1
    fibsum = 0
    for i in range(1, n+1):
        fibsum = fib2 + fib1
        if i > 1:
            fib1 = fib2
            fib2 = fibsum
    print(fibsum)
        

"""
Problem:

    The triangle numbers are: 1, 3, 6, 10, 15, 21, 28, ...
    They are generated by starting at 0 and going up by 1,
    then adding one more to the difference each time.

    The function triangle_numbers takes an integer n,
    and should then print the nth triangle number.

Tests:

    >>> triangle_number(1)
    1
    >>> triangle_number(3)
    6
    >>> triangle_number(7)
    28
    >>> triangle_number(50)
    1275

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def triangle_number(n):
    up = 1
    x = 0
    for i in range(0, n+1, up):

       
        if i == n:
            print(x)
        else:
            x = x+up
            up = up+1
        
    

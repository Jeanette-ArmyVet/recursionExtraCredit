def power(x, n):
    
    """
    Computes the value of x raised to the power of n, using recursion.
    Assumes that n is an even and non-negative integer.
    """
    
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
    

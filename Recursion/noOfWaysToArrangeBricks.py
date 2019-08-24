def noOfWays(n):
    """Number of Ways to Arrange bricks of size 1*2 in a board of size 2*n"""
    if n == 1: return 1
    if n == 2: return 2
    return noOfWays(n-1) + noOfWays(n-2)

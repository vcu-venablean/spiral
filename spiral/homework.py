def spiralize(number):
    """Initializing the variable I need for the spiral loop"""
    n = 1
    step = 2
    total = 0
    since_last = 0
    """A While loop that builds the spiral and sums up the diagonals"""
    while n <= number ** 2:
        total += n
        n += step
        since_last += 1
        if since_last == 4:
            step += 2
            since_last = 0
    """Total is the variable I used that adds up the diagonals of the spiral and gets returned"""
    return total


"""Printing the sum of the diagonals of a 501 by 501 spiral"""
print(spiralize(501))

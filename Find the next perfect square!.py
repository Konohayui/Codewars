def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    n = sq ** (0.5)
    if n > 0 and sq % n == 0:
        return (n + 1)**2
    else:
        return -1

def find_next_square(sq):
    from math import sqrt, modf
    
    # Return the next square if sq is a square, -1 otherwise
    if modf(sqrt(sq))[0] == 0:
        next_perfect_square = (sqrt(sq)+1)**2
        return next_perfect_square
    else:
        return -1

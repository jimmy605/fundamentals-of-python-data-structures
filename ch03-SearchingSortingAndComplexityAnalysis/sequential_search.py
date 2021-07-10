def sequentitalSearch(target, lyst):
    """Returns the position of the target item if found, or -1 otherwise."""
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1
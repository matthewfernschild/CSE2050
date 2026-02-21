def dist(n):
    """
    creates a set of N. if set of n is smaller than n, then n has duplicates
    
    we are given n, a list of ints, if any num in n repeats, then return false
    """
    tester = set(n)
    if len(tester) == len(n):
        return True
    return False
    

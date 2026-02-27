def solve_puzzle(L): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    idx = 0
    goal = len(L) - 1

    visiting = set()

    if idx == -1 :
        return True
    else:
        idx += L[idx]
        
    return _solve_puzzle(L,idx=0,visited=set())
# if current index == lst[-1], then we solved the puzzle


def _solve_puzzle(L,idx,visited):
    """"""
    if idx == -1:
        return True


solve_puzzle([3, 6, 4, 1, 3, 4, 2, 0])
def solve_puzzle(L): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    visited = set()
    return _solve_puzzle(L,0,visited)

def _solve_puzzle(L,idx,visited):
    ''' the internal puzzle solver'''
    goal = len(L) - 1

    if idx == goal: # winner winner
        return True
    
    if idx in visited:
        return False
    visited.add(idx)


    tiles = L[idx] # of tiles to move

    if tiles == 0:
        return False
    
    clockwise = (idx + tiles) % len(L)
    counterclockwise = (idx - tiles) % len(L)

    return _solve_puzzle(L,clockwise,visited) or _solve_puzzle(L,counterclockwise,visited)
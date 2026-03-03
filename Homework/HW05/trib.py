def trib(k):
    '''tribonacci sequence'''
    seen = {
        1:0,
        2:0,
        3:1
    }
    return _trib(k,seen)

def _trib(k,seen):
    ''' the recursive solver'''
    if k in seen:
        return seen[k]
    seen[k] = _trib(k-1,seen) + _trib(k-2,seen) + _trib(k-3,seen)

    return seen[k]

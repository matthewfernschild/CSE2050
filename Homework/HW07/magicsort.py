import math
from enum import Enum

INVERSION_BOUND = 10  # pre-defined constant; independent of list input sizes

class MagicCase(Enum):
    """Enumeration for tracking which case we want to use in magicsort"""
    GENERAL = 0
    SORTED = 1
    CONSTANT_INVERSIONS = 2
    REVERSE_SORTED = 3

def linear_scan(L):
    num = 0
    for i in L:
        if (L[i]>L[i+1]):
           num += 1 
    return num

def reverse_list(L, alg_set=None):
    num = 0
    for i in L:
        if (L[i]>L[i+1]):
           num += 1 
    return num
    

def magic_insertionsort(L, left, right, alg_set=None):
    pass

def magic_mergesort(L, left, right, alg_set=None):
    pass

def magic_quicksort(L, left, right, depth=0, alg_set=None):
    pass

def magicsort(L):
    pass

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
    for i in range(0,len(L)-1):
        if (L[i]>L[i+1]):
           num += 1 
    if num == len(L)-1:
        return MagicCase.REVERSE_SORTED
    if num == 0:
        return MagicCase.SORTED
    if num <= INVERSION_BOUND:
        return MagicCase.CONSTANT_INVERSIONS
    return MagicCase.GENERAL


def reverse_list(L, alg_set=None):
    L[:] = L[::-1]
    alg_set.add("magic_insertionsort")
    return L

def magic_insertionsort(L, left, right, alg_set=None):
    for i in range(left+1,right):
        curr = i
        while curr > left and L[curr] < L[curr - 1]:
            L[curr], L[curr - 1] = L[curr - 1], L[curr]
            curr -= 1
    alg_set.add("magic_insertionsort")
    return L

def magic_mergesort(L, left, right, alg_set=None):
    if left >= right:
        return L

    mid = (left + right) // 2

    magic_mergesort(L, left, mid)
    magic_mergesort(L, mid + 1, right)

    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if L[i] <= L[j]:
            temp.append(L[i])
            i += 1
        else:
            temp.append(L[j])
            j += 1

    while i <= mid:
        temp.append(L[i])
        i += 1

    while j <= right:
        temp.append(L[j])
        j += 1

    for k in range(len(temp)):
        L[left + k] = temp[k]
    alg_set.add("magic_mergesort")
    return

def magic_quicksort(L, left, right, depth=0):
    size = right - left

    if size <= 1:
        return

    if size <= 20:
        magic_insertionsort(L, left, right)
        return

    if depth > 3 * (math.log2(len(L)) + 1):
        magic_mergesort(L, left, right)
        return
    
    pivot_index = right - 1
    pivot_value = L[pivot_index]

    i = left
    for j in range(left, right - 1):
        if L[j] < pivot_value:
            L[i], L[j] = L[j], L[i]
            i += 1

    L[i], L[pivot_index] = L[pivot_index], L[i]

    magic_quicksort(L, left, i, depth + 1)
    magic_quicksort(L, i + 1, right, depth + 1)

    return L

def magicsort(L):
    alg_set = set()
    case = linear_scan(L)
    
    if case == MagicCase.SORTED:
        return alg_set
    
    if case == MagicCase.REVERSE_SORTED:
        alg_set.add("reverse_list")
        reverse_list(L)
        return alg_set
    
    if case == MagicCase.CONSTANT_INVERSIONS:
        alg_set.add("magic_insertionsort")
        magic_insertionsort(L,0,len(L))
        return alg_set
    
    alg_set.add("magic_quicksort")
    magic_quicksort(L,0,len(L))
    return alg_set

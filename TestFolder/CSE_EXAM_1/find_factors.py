# Code to prepare for Midterm 1

"""
Part a: find_factors.py

Write function find_factors that takes a list of positive integers as input and returns a dictionary. 
In the dictionary, each key should be a number from the input list, and the corresponding value should be a 
list containing all the factors of that number within the input list.

For clarification, factors are numbers that evenly divide into another number without leaving a remainder. 
For example, all factors of 24 are: 1, 2, 3, 4, 6, 8, 12, and 24.

Example:

For the input list: [6, 7, 18, 1, 3]

The function should return:

{6: [6, 1, 2, 3], 7: [7, 1], 18: [6, 9, 18, 1, 2, 3], 1: [1], 3: [1, 3]}
"""

def find_factors(lst):
    ans = dict()
    for num in lst:
        i = 1
        factors = []

        while i <= num:
            if num % i == 0:
                factors.append(i)
            i += 1
        ans[num] = factors
    return ans
    
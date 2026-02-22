#The Problem: 
# #Given a list of numbers nums and a target integer, 
# return the indices of the two numbers such that they add up to the target.

# slow version, 3n^2
def two_sum(L,target):
    for num in L: # n
        for t in L: # n * 3
            if (num+t) == target:
                return f"{num} + {t} = {target}"
    
    return "No 2 numbers equal the target."

nums = [2, 7, 11, 15]
print(two_sum(nums,9))
# O(n^2)

def two_sum(L,target):
    undupe = set(L) # +1, removes possible duplicates so we only have to check options once

    for num in undupe: # n
        if (target-num) in undupe: # *3, +2
            num2 = target-num 
            return f"{num} + {num2} = {target}"
    
    return "No 2 numbers equal the target."
        
# O(n), 3n+3
print(two_sum(nums,9))


# Here is the perfect way to do it: (Courtesy of Gemini)
def two_sum_indices(nums, target):
    # Dictionary to store: {Number: Index}
    prev_map = {} 

    for i, n in enumerate(nums):
        diff = target - n
        
        # Check if the number we need is already in our dictionary
        if diff in prev_map:
            return [prev_map[diff], i] # Returns the indices
        
        # If not found, "remember" this number and its index for later
        prev_map[n] = i
        
    return []

# Test
nums = [2, 7, 11, 15]
print(two_sum_indices(nums, 9)) # Output: [0, 1]


# so they add to a dictionary as they go. I created a full dictionary.
# they immediately looked for the difference, then 

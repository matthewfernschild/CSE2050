# This program generates a list of numbers and writes them to a file.
##### Generate list of numbers #####
n = 2000  # Max is 2000 due to memory constraints on the gradescope
          # containers that run your submissions
#L = list(range(n, 0, -1))   # [1000, 999, 998, ..., 1]

import random

L = list(range(n+1, 1, -1))


# Random list with only values 1 through 3
#random_1_to_3 = [random.randint(1, 3) for _ in range(n)]

##### Create file to write to #####
f = open("numbers.txt", "w")

##### Write numbers to file #####
for item in L:
    f.write(str(item))
    f.write(" ")

#### Close the file ####
f.close()
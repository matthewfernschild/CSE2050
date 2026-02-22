# 12/20/2025, Day 1 of practicing code to get into a company where i can learn from really smart people

# Gemini's Syntax Warmup
#1. A for-loop: Print every number from 1 to 20, but only if it's even.
for num in range(1,21):
    if (num % 2) == 0:
        print(num)

#2. A list manipulation: Create a list of 5 colors. Add a 6th color to the end. Remove the 2nd color.
colors = ["red","blue","green","yellow","pink"]
print(colors)

colors.append("neon green")
print(colors)

# to delete use "del" or pop()
del colors[1]
print(colors)

#3. A function: Write a function greet(name) that returns "Hello, [name]".
name = "name"
def greet(name) :
    print(f"Hello, {name}")
greet(name)


# Part 2
# Goal: Solve the "Duplicate Check" problem using logic, even if it's "slow" logic.

num_list = [1,1,2,3,3,4,5]


# def isDuplicate(nums):
 #   num_dict = {}
#        # seen = set()
  #  for num in nums:
  #      if num in num_dict:
#            num_dict[num] +=1
 #           # they wanted "return True"
 #       # then instead of else, seen.add(num)
  #      else:
   #         num_dict[num] = 1
    # then instead of a second loop, just return False
    # if the first for loop finishes, then no duplicates were found
    # we are checking the list for any duplicates, not labelling each as a duplicate or not
#    for num in nums:
     #   if num_dict[num] > 1:
           # print("True")
      #  else:
       #     print("False")
        

# isDuplicate(num_list)

# for each number in the list, compare it to each other number in the list.
# this should look like
# for number in numberlist:
# if number is equal to number selected in comparison
# add 1 to the variable
# 
# i could do this with a dictionary where each key is the number
# then each value is the amount of times its there



# now im going to read sheehys book on Big O then try and redo this.



def isDuplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    
isDuplicate(num_list)
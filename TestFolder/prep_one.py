# Write a Python function that takes a list of numbers and returns 
# True if any number appears at least twice in the list, and False if every element is distinct.


thelist = [2,3,2,24,5,1,1,4,2,5,23,32,4,5,6,2,2,4]


def isDuplicate():
    testlist = []
    for num in thelist:
        if num not in testlist:
            testlist.append(num)

    for item in thelist:
        if item in testlist:
            print(True)
        else:
            testlist.append(num)
            print(False)

isDuplicate()




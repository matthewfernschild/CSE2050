#Below is a program that adds up the first k positive integers and returns
#both the sum and time required to do the computation.

#inefficient way to do this
def sumofk(k):
    total = 0

    for i in range (k+1):
        total = total + i
    
    return total

print(sumofk(3))

# turn it into a series and use that. k(k+1)/2

def sumk(k):
    return (k*(k+1)//2)

print(sumk(3))
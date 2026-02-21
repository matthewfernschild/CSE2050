###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up your classmates . If you do so, remember not to #
# share code directly. Discussions are fine, code sharing is not. Also note   #
# that all have to submit individually.                                       #
###############################################################################

def fizz_buzz(start, finish):
    # Delete this comment and below, then start working.
    # Make sure you add a docstring to this function.
    """fizz is when divisible by 3 or has 3 
        buzz is when divisible by 5 or has 5
        fizzbuzz is when both are true.
        I turned fizz & buzz to bool variables for readability"""
    
    for i in range(start,finish+1):
        
        fizz = i % 3 == 0 or "3" in str(i)
        buzz = i % 5 == 0 or "5" in str(i)

        if fizz and buzz:
            print("fizzbuzz")
        elif fizz:
            print("fizz")
        elif buzz:   
            print("buzz")
        else:
            print(i)

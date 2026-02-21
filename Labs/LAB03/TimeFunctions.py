import time

def time_function(func,args,n_trials=10): # minimum trials of 10, suggested by chat
    """Basic Time Function. start - end = total time"""
    
    start_time = []
    end_time = []

    total_time = float('inf')

    for n in range(n_trials):

        start_time.append(time.time())
        func(args)
        end_time.append(time.time())
        
        new_time = end_time[-1]-start_time[-1]

        if new_time < total_time:
            total_time = new_time

    return total_time
    
def time_function_flexible(func,args_tuple,n_trials=10):
    """Time, but with multi-arg functionality. (put args in a tuple)"""
    
    start_time = []
    end_time = []

    total_time = float('inf')

    for n in range(n_trials):

        start_time.append(time.time())
        func(*args_tuple)
        end_time.append(time.time())
        
        new_time = end_time[-1]-start_time[-1]

        if new_time < total_time:
            total_time = new_time

    return total_time

if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    def test_func2(L,L2):
        for item in L:
            item *= 2
        for item in L2:
            item *= 2
        
# REGULAR FUNC
    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2) 

# FLEXIBLE FUNC
    L3 = [i for i in range(10**5)]
    t3 = time_function_flexible(test_func2, (L3,L3))

    L4 = [i for i in range(10**6)] # should be 20x slower to operate on every item
    t4 = time_function_flexible(test_func2, (L4,L4))



    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))
    print("t(L3,L3) = {:.3g} ms".format(t3*1000))
    print("t(L4,L4) = {:.3g} ms".format(t4*1000))
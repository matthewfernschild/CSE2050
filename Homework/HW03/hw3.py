import random 
import time

def generate_lists(size):
    list1 = random.sample(range(0, size*2), size)
    list2 = random.sample(range(0, size*2), size)
    
    return list1, list2


def find_common(list1, list2): # O(n^2)
    common = 0 
    for i in list1: # O(N)
        if i in list2: # O(N) at worst, linear search
            common += 1

    return common
        

def find_common_efficient(list1, list2): # O(n+m), but len(n) = len(m), so its actually O(n)    
    return len(set(list1) & set(list2))

def measure_time():
    sizes = [10,100,1000,10000,100000,1000000]

    print("{:<12}{:<22}{:<30}".format("List Size", "find_common Time (ms)", "find_common_efficient Time (ms)"))
    print("{:<12}{:<22}{:<30}".format("-"*9, "-"*19, "-"*28))
        
    for n in sizes:
        l1,l2 = generate_lists(n)
        if n <= 1000000:
            start_time = time.time()
            find_common(l1,l2)
            end_time = time.time()
            t_common = (end_time - start_time)*1000
        else:
            t_common = float('inf')
        start_time = time.time()
        find_common_efficient(l1,l2)
        end_time = time.time()
        t_eff = end_time - start_time
        
        print("{:<12}{:<22.3f}{:<30.3f}".format(n, t_common, t_eff*1000))


if __name__ == "__main__":
    measure_time()




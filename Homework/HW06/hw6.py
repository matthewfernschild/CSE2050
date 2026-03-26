import random
import time


# TODO: Implement bubble_sort function.
# Ensure it is adaptive
def bubble_sort(L):
    swaps = 0
    for i in range(0, len(L)):
        swapped = False
        for j in range(0, len(L) - 1 - i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return L, swaps

# TODO: Implement insertion_sort function.
# Ensure it is adaptive
def insertion_sort(L):
    swaps = 0
    for i in range(1,len(L)):
        j = i - 1
        while j >= 0 and L[j + 1] < L[j]:
            temp_arr = L[j + 1]
            L[j + 1] = L[j]
            L[j] = temp_arr
            swaps += 1
            j -= 1
    return L, swaps
    

# TODO: Implement selection_sort function.
# Ensure it is adaptive
def selection_sort(L):
    swaps = 0
    for i in range(0,len(L)):
        ind = i
        for j in range(i+1, len(L)):
            if L[j] < L[ind]:
                ind = j
        if ind != i:
            L[i], L[ind] = L[ind], L[i]
            swaps += 1
    
    return L, swaps


#Feel free to write any additional functions that may be necessary 
# to populate the results required in part 2.
def case_random(n):
    L = list(range(1, n + 1))
    random.shuffle(L)
    return L


def case_sorted(n):
    return list(range(1, n + 1))


def case_reverse(n):
    return list(range(n, 0, -1))


def case_move_end_to_front(n):
    L = list(range(1, n + 1))
    k = int(n * 0.05)
    return L[-k:] + L[:-k]


def case_move_front_to_end(n):
    L = list(range(1, n + 1))
    k = int(n * 0.05)
    return L[k:] + L[:k]

def run_one_sort(sort_function, original_list):
    L_copy = original_list[:]
    start = time.perf_counter()
    sorted_list, swaps = sort_function(L_copy)
    end = time.perf_counter()
    return swaps, end - start

def print_results_table(results):
    print("Performance Analysis of Sorting Algorithms")
    print("-" * 110)
    print(f"{'Scenario':<22}{'List Size':<12}{'Bubble Sort':<24}{'Insertion Sort':<24}{'Selection Sort':<24}")
    print(f"{'':<22}{'':<12}{'Swaps, time':<24}{'Swaps, time':<24}{'Swaps, time':<24}")
    print("-" * 110)

    for row in results:
        scenario, size, bubble_data, insertion_data, selection_data = row
        print(f"{scenario:<22}{size:<12}{str(bubble_data):<24}{str(insertion_data):<24}{str(selection_data):<24}")

    print("-" * 110)


# ---------------------------
# Main experiment
# ---------------------------

def run_analysis():
    sizes = [2000, 3000, 4000, 5000, 6000]
    results = []

    scenarios = [
        ("Random", case_random),
        ("Sorted", case_sorted),
        ("Reverse", case_reverse),
        ("Move end to front", case_move_end_to_front),
        ("Move front to end", case_move_front_to_end)
    ]

    for scenario_name, scenario_function in scenarios:
        for size in sizes:
            test_list = scenario_function(size)

            bubble_result = run_one_sort(bubble_sort, test_list)
            insertion_result = run_one_sort(insertion_sort, test_list)
            selection_result = run_one_sort(selection_sort, test_list)

            bubble_result = (bubble_result[0], round(bubble_result[1], 5))
            insertion_result = (insertion_result[0], round(insertion_result[1], 5))
            selection_result = (selection_result[0], round(selection_result[1], 5))

            results.append((scenario_name, size, bubble_result, insertion_result, selection_result))

    print_results_table(results)

if __name__ == "__main__":
    run_analysis()
    



'''
Part 3: Conclusion

Based on your performance analysis, write a conclusion that addresses the following points:

1. Provide a ranking of the sorting algorithms based on their performance in each scenario.
   Which sorting algorithm performed best in each case (Random, Sorted, Reverse Order, Move
   End to Front, Move Front to End), and why do you think it performed better?
    Best at:
    Random - Selection Sort
        When lists are random selection sort wins because it is the fastest overall.
    Sorted - Bubble Sort
        Bubble sort is the fastest on sorted because it stops early
    Reversed Order - Selection Sort
        Selection sort wins because it only need to swap the out of place numbers one at a time, whereas the other two need to swap over and over again
    Move End to Front - Bubble Sort
        Bubble wins because the list is mostly sorted and it can keep pushing the out of place numbers to the end
    Move Front to End - Insertion Sort
        insertion sort wins because its the quickest at moving from the end to the front instead of swapping places over and over again. 

   
2. Explain how the number of swaps made by each algorithm affects both efficiency and time
   complexity across different scenarios.
    The # of swaps lowers efficiency, but can be quicker depending on the algorithm and data. When you have a randomized list, solving it in the least swaps is the best approach, 
    but if you have an already sorted or mostly sorted list than the method the algorithm uses is more important to the time it taken than the number of swaps. 
    For example, in the mostly sorted lists, even though Selection Sort is theoretically more efficient, it loses to Bubble & Insertion because they're more adaptive.

3. Discuss the impact of the initial order of data on how well each algorithm performs.
   Explain why some algorithms perform differently on sorted, reversed, or random lists.
    Whether or not an algorithm is adaptive or not will affect the time it takes to complete a sort based on the initial order of the data. 
    An adaptive algorithm will be much quicker than a non-adaptive algorithm (even if it has a faster big O notation), if the initial order of the list is mostly or completely sorted. As seen by the 5% in front / back and pre-sorted tests.

'''

'''
Include the results table here
Example:
Performance Analysis of Sorting Algorithms
--------------------------------------------------------------------------------------------------------------
Scenario              List Size   Bubble Sort             Insertion Sort          Selection Sort
                                  Swaps, time             Swaps, time             Swaps, time
--------------------------------------------------------------------------------------------------------------
Random                2000        (1003025, 0.14292)      (1003025, 0.11145)      (1993, 0.05799)
Random                3000        (2207837, 0.33538)      (2207837, 0.24012)      (2991, 0.13252)
Random                4000        (3931049, 0.55781)      (3931049, 0.4348)       (3995, 0.2761)
Random                5000        (6164230, 0.90691)      (6164230, 0.68043)      (4992, 0.36202)
Random                6000        (9065870, 1.28489)      (9065870, 0.99482)      (5994, 0.52282)
Sorted                2000        (0, 7e-05)              (0, 0.00012)            (0, 0.05727)
Sorted                3000        (0, 0.00011)            (0, 0.00018)            (0, 0.13048)
Sorted                4000        (0, 0.00015)            (0, 0.00024)            (0, 0.2314)
Sorted                5000        (0, 0.00019)            (0, 0.00031)            (0, 0.36864)
Sorted                6000        (0, 0.00023)            (0, 0.00037)            (0, 0.74575)
Reverse               2000        (1999000, 0.18787)      (1999000, 0.21004)      (1000, 0.06058)
Reverse               3000        (4498500, 0.4268)       (4498500, 0.474)        (1500, 0.14647)
Reverse               4000        (7998000, 0.78302)      (7998000, 0.87084)      (2000, 0.24405)
Reverse               5000        (12497500, 1.24189)     (12497500, 1.37831)     (2500, 0.37861)
Reverse               6000        (17997000, 1.77535)     (17997000, 2.12835)     (3000, 0.59013)
Move end to front     2000        (190000, 0.01881)       (190000, 0.02085)       (1900, 0.05868)
Move end to front     3000        (427500, 0.0436)        (427500, 0.0498)        (2850, 0.13179)
Move end to front     4000        (760000, 0.07663)       (760000, 0.08469)       (3800, 0.23277)
Move end to front     5000        (1187500, 0.12501)      (1187500, 0.13386)      (4750, 0.37359)
Move end to front     6000        (1710000, 0.17221)      (1710000, 0.18812)      (5700, 0.5211)
Move front to end     2000        (190000, 0.08148)       (190000, 0.0202)        (1900, 0.05819)
Move front to end     3000        (427500, 0.18568)       (427500, 0.04552)       (2850, 0.13055)
Move front to end     4000        (760000, 0.33753)       (760000, 0.08144)       (3800, 0.23389)
Move front to end     5000        (1187500, 0.52483)      (1187500, 0.14088)      (4750, 0.36168)
Move front to end     6000        (1710000, 0.76957)      (1710000, 0.19087)      (5700, 0.56556)
--------------------------------------------------------------------------------------------------------------
'''

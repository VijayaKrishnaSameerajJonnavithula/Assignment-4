import time
import random
from Heap import heapsort
# Sample implementations of Quicksort and Merge Sort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Timing utility
def time_sorting_algorithm(algorithm, arr):
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    return end_time - start_time

# Test on different input types and sizes
sizes = [1000, 5000, 10000]
input_types = ["random", "sorted", "reverse"]

for size in sizes:
    for input_type in input_types:
        if input_type == "random":
            arr = [random.randint(0, 100000) for _ in range(size)]
        elif input_type == "sorted":
            arr = list(range(size))
        elif input_type == "reverse":
            arr = list(range(size, 0, -1))
        
        arr_copy = arr.copy()
        print(f"Size: {size}, Input: {input_type}")
        print("Heapsort:", time_sorting_algorithm(heapsort, arr.copy()))
        print("Quicksort:", time_sorting_algorithm(quicksort, arr.copy()))
        print("Merge Sort:", time_sorting_algorithm(merge_sort, arr_copy))
        print()

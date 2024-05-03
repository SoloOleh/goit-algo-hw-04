import timeit
import random

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged, left_index, right_index = [], 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def python_timsort(arr):
    return sorted(arr)

test_data_sizes = [100, 1000, 10000]
results = []

for size in test_data_sizes:
    data = [random.randint(0, 1000) for _ in range(size)]
    insertion_sort_time = timeit.timeit('insertion_sort(data.copy())', globals=globals(), number=1)
    merge_sort_time = timeit.timeit('merge_sort(data.copy())', globals=globals(), number=1)
    python_timsort_time = timeit.timeit('python_timsort(data.copy())', globals=globals(), number=1)
    results.append(f'Test data size: {size}, Insertion sort time: {insertion_sort_time}, Merge sort time: {merge_sort_time}, Phyton timsort time: {python_timsort_time}')

results

print(results)  

"""
Test data size: 100, Insertion sort time: 0.00010254199150949717, Merge sort time: 8.512497879564762e-05, Phyton timsort time: 8.041970431804657e-06, 
Test data size: 1000, Insertion sort time: 0.011608750035520643, Merge sort time: 0.0010459170443937182, Phyton timsort time: 7.887498941272497e-05, 
Test data size: 10000, Insertion sort time: 1.23389741696883, Merge sort time: 0.012771415989845991, Phyton timsort time: 0.0009039579890668392.
"""

""" 
Timsort ефективно використовує переваги обох сортувань: вставками на малих сегментах даних та злиттям для більших. 
Це робить його швидким і ефективним навіть на великих масивах. 
Тому більшість людей використовують вбудовані алгоритми сортування в Python, а не пишуть свої. 
"""
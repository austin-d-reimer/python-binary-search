from binary_search import binary_search, display_results
from random_sorted_array import create_random_sorted_array

arr = [2, 3, 4, 10, 40, 45]
target = 46

result, iteration = binary_search(arr, target)

display_results(result, iteration, target)

arr = create_random_sorted_array(1_000_000, 50_000)
target = arr[1200]

result, iteration = binary_search(arr, target)
display_results(result, iteration, target)

from binary_search import search
from random_sorted_array import create_random_sorted_array

arr = [2, 3, 4, 10, 40, 45]
target = 46

search(arr, target)

arr = create_random_sorted_array(1_000_000, 50_000)
target = arr[1200]

search(arr, target)

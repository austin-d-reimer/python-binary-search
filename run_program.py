from binary_search import binary_search, display_results

arr = [2, 3, 4, 10, 40, 45]
target = 46

result, iteration = binary_search(arr, target)

display_results(result, iteration, target)

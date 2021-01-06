from random_sorted_array import create_random_sorted_array


def display_results(result, iteration):
    if result != -1:
        print(f"{target} found at {result} in {iteration} iterations")
    else:
        print(f"{target} not found after {iteration} iterations")


def binary_search(arr, target):
    """
    Search through an array of data using the binary search method.
    """
    start = 0
    end = len(arr) - 1
    iteration = 1
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid, iteration
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        iteration = iteration + 1
    # Not found
    return -1, iteration - 1


arr = [2, 3, 4, 10, 40, 45]
target = 46

result, iteration = binary_search(arr, target)

display_results(result, iteration)

from binary_search import search
from random_sorted_array import create_random_sorted_array


def user_search():
    search(arr2, int(input("Number to search for ")))

    user_input = input("Do you want to continue Y or n ")

    if user_input == "n":
        print("Good bye")
        return
    else:
        user_search()


arr1 = [2, 3, 4, 10, 40, 45]
target1 = 46

search(arr1, target1)

arr2 = create_random_sorted_array(1_000_000, 100_000)
target2 = arr2[1200]

print(
    f"""
length {len(arr2)}
max {arr2[-1]}
"""
)

search(arr2, target2)

user_search()

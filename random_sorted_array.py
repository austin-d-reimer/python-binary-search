import random


def create_random_sorted_array():
    arr = random.sample(range(10000000), k=1000000)
    arr.sort()
    return arr

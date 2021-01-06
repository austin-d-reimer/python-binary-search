import random


def create_random_sorted_array():
    arr = random.sample(range(1_000_000), k=1_000_000)
    return arr.sort()

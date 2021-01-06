import random


def create_random_sorted_array(max, length):
    """
    Creates a random sorted array with a set max number size and length.
    """
    arr = random.sample(range(max), k=length)
    arr.sort()
    return arr

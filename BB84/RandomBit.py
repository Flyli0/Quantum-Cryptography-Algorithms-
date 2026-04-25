import random


def random_bit():  # returns a random bit
    i = random.randint(0, 100)
    if i % 2 == 0:
        return 0
    else:
        return 1

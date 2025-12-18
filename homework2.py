import random

def get_numbers_ticket(min, max, quantity):
    # check
    if min < 1 or max > 1000 or min >= max:
        return []

    if quantity > (max - min + 1):
        return []

    # generate num
    numbers = random.sample(range(min, max + 1), quantity)

    # sort
    return sorted(numbers)
result = get_numbers_ticket(1, 49, 6)
print(result)
#!/usr/bin/python

import sys
cache = {}


def making_change(amount, denominations):
    print(amount)
    count = 0
    if amount == 0:
        return 1
    for i in range(len(denominations)):
        if denominations[i] <= amount:
            count += making_change(amount -
                                   denominations[i], denominations[i:])

    return count


# if __name__ == "__main__":
#     # Test our your implementation from the command line
#     # with `python making_change.py [amount]` with different amounts
#     if len(sys.argv) > 1:
#         denominations = [1, 5, 10, 25, 50]
#         amount = int(sys.argv[1])
#         print("There are {ways} ways to make {amount} cents.".format(
#             ways=making_change(amount, denominations), amount=amount))
#     else:
#         print("Usage: making_change.py [amount]")
print(making_change(10, [1, 5, 10, 25, 50]))

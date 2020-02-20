#!/usr/bin/python

import argparse


def find_max_profit(prices):

    min_price = prices[0]
    max_price = prices[-1]
    max_index = len(prices) - 1
    for i in range(1, len(prices) - 1):
        if prices[i] < min_price and i < max_index:
            min_price = prices[i]
            for j in range(max_index, i, -1):
                if prices[j] > max_price:
                    max_price = prices[j]
                    max_index = j

    return max_price - min_price


# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))

print(find_max_profit([10, 50, 5, 45, 5, 100, 0]))

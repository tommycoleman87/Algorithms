#!/usr/bin/python

import argparse


def find_max_profit(prices):

    min_price = prices[0]
    min_index = 0
    max_index = len(prices) - 1
    max_price = prices[max_index]
    for i in range(1, len(prices)):
        if prices[i] < min_price and i < max_index:
            min_price = prices[i]
            min_index = i
        elif prices[i] > max_price and i > min_index:
            max_price = prices[i]
            max_index = i

    return max_price - min_price


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

#!/usr/bin/python

import sys


def rps_helper(args):
    plays = []
    for play in args:
        rock = list(play)
        rock.append('rock')
        paper = list(play)
        paper.append('paper')
        scissors = list(play)
        scissors.append('scissors')
        plays.append(rock)
        plays.append(paper)
        plays.append(scissors)

    return plays


def rock_paper_scissors(n):
    plays = [['rock'], ['paper'], ['scissors']]
    if n == 0:
        return [[]]
    while n > 1:
        n = n - 1
        plays = rps_helper(plays)
        rock_paper_scissors(n)

    return plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

print(rps_helper([['rock'], ['paper'], ['scissors']]))

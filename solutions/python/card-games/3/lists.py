"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

import statistics


def get_rounds(number):
    return [number, number +1, number +2]


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    if number in rounds:
        return True
    return False


def card_average(hand):
    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    first_last_avg = (hand[0] + hand[-1])/2
    middle_card = statistics.median(hand)
    if first_last_avg == card_average(hand):
        return True
    if middle_card == card_average(hand):
        return True
    return False


def average_even_is_average_odd(hand):
    even_index = hand[::2]
    odd_index = hand[1::2]
    if sum(even_index)/len(even_index) == sum(odd_index)/len(odd_index):
        return True
    return False


def maybe_double_last(hand):
    if hand[-1] == 11:
        return hand[:-1] + [22]
    return hand
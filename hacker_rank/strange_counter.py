#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#


def strangeCounter(t):
    if t < 1:
        raise ValueError("t must be a positive integer")

    if 1 <= t <= 3:
        return 4 - t

    if t > 3:
        initial_number_prior_cycle = 3 * 2
        current_value = initial_number_prior_cycle
        start_time = 4
        end_time = t + 3

        for time in range(start_time, end_time + 1):
            if time == t:
                break

            current_value -= 1

            if current_value < 1:
                initial_number_prior_cycle = initial_number_prior_cycle * 2
                current_value = initial_number_prior_cycle

        return current_value


print("3", strangeCounter(3))
print("4", strangeCounter(4))
print("5", strangeCounter(5))
print("6", strangeCounter(6))
print("7", strangeCounter(7))
print("8", strangeCounter(8))
print("9", strangeCounter(9))
print("10", strangeCounter(10))
print("13", strangeCounter(13))

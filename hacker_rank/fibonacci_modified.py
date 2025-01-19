#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#


def fibonacciModified(t1, t2, n):
    for _ in range(n - 2):
        t_next = t1 + t2**2
        t1 = t2
        t2 = t_next
    return t2


print(fibonacciModified(0, 1, 5))
print(fibonacciModified(0, 1, 6))

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import product

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#


def get_combinations(n):
    combinations = ["".join(combo) for combo in product("35", repeat=n)]
    return [int(num) for num in combinations]


def check_3s_and_5s(num):
    return num.count("3") % 5 == 0 and num.count("5") % 3 == 0


def decentNumber(n):
    if n < 1:
        raise ValueError("The number length must be a positive integer")

    # Obtener todas las combinaciones posibles de 3s y 5s (producto cartesiano)
    combinations = get_combinations(n)
    # Ordenar las combinaciones de mayor a menor
    combinations.sort(reverse=True)
    # Flag para saber si se encontro una combinacion que cumpla con las condiciones
    found = False
    # Iterar sobre las combinaciones
    for combination in combinations:
        # Si la combinacion cumple con las condiciones, imprimir la combinacion y terminar el ciclo
        if check_3s_and_5s(str(combination)):
            print(combination)
            found = True
            break
    # Si no se encuentra ninguna combinacion que cumpla con las condiciones, imprimir -1
    if not found:
        print("-1")


decentNumber(4)
decentNumber(1)
decentNumber(3)
decentNumber(5)
decentNumber(11)

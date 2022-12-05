#Working with functions

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Calculate the tip
    tip = meal_cost * (tip_percent/100)
    # Calculate the tax
    tax = meal_cost * (tax_percent/100)
    # Calculate the total cost
    total_cost = meal_cost + tip + tax
    # Rounded final cost
    total_cost = round(total_cost)
    print(total_cost)
    

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
#!/usr/bin/env python3

"""
Name: Dice Roller.py
Project Number: 2
Author: Christian M
Date: Aug 6, 2022
"""

from random import randint

def roll():
    return randint(1,6)

if __name__ == "__main__":
    print(roll())
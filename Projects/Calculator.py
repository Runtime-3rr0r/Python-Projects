#!/usr/bin/env python3

"""
Name: Calculator.py
Project Number: 1
Author: Christian M
Date: Aug 6, 2022
"""

def calculate(expression):
    try:
        ans = eval(int(expression))
        return ans
    except ValueError:
        return 'Invalid Expression\nquitting...'

if __name__ == '__main__':
    print(calculate(input('Enter expression: ')))
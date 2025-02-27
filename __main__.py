#!/bin/env python
import re

NUMBER = r'(?:\d+(?:\.\d+)?)'   # No groups
ADDITIVE_OPE = r'[+-]'          # No groups
ADDITIVE_EXP = rf'(?:((?:{NUMBER}{ADDITIVE_OPE})*{NUMBER})({ADDITIVE_OPE})({NUMBER}))'
    # Groups: (left-number-or-expression, operator, right-number)

def math_eval(expression: str):

    if re.match(rf'^{NUMBER}$', expression):
        return float(expression)

    m = re.match(rf'^{ADDITIVE_EXP}$', expression)
    if m:
        if m[2] == '+':
            return math_eval(m[1]) + float(m[3])
        elif m[2] == '-':
            return math_eval(m[1]) - float(m[3])

while True:
    expression = input("> ")
    result = math_eval(expression)
    if int(result) == result:
        print(int(result))
    else:
        print(result)
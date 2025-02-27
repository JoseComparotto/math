#!/bin/env python
import re

NUMBER_PATTERN = r'\d+(?:\.\d+)?'
SUM_EXP_PATTERN = rf'((?:{NUMBER_PATTERN}\+)*{NUMBER_PATTERN})\+({NUMBER_PATTERN})'

def math_eval(expression: str):

    if re.match(rf'^{NUMBER_PATTERN}$', expression):
        return float(expression)

    m = re.match(rf'^{SUM_EXP_PATTERN}$', expression)
    if m:
        return math_eval(m[1]) + float(m[2])

while True:
    expression = input("> ")
    result = math_eval(expression)
    if int(result) == result:
        print(int(result))
    else:
        print(result)
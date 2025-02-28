#!/bin/env python
import re

NUMBER = r'(?:\d+(?:\.\d+)?)'
VALID_EXPRESSION = rf'^\s*{NUMBER}\s*(?:[*/+-]{NUMBER}\s*)*$'

def number_solve(expression):

    m = re.match(rf'^\s*({NUMBER})\s*$', expression)
    if not m:
        raise ValueError("Expressão inválida! Não foi possivel resolver valor.")

    return float(m[1])

def multiplicative_solve(expression):

    match = re.match(r'^(.+)([*/])(.+?)$', expression)
    if not match:
        return number_solve(expression)

    left, ope, right = match.groups()

    left = multiplicative_solve(left)
    right = number_solve(right)
   
    if ope == '*':
        return left * right
        
    if ope == '/':
        return left / right

def additive_solve(expression):

    match = re.match(r'^(.+)([+-])(.+?)$', expression)
    if not match:
        return multiplicative_solve(expression)

    left, ope, right = match.groups()

    left = additive_solve(left)
    right = multiplicative_solve(right)
   
    if ope == '+':
        return left + right
        
    if ope == '-':
        return left - right

def math_eval(expression: str):
    
    if not re.match(VALID_EXPRESSION, expression):
        raise ValueError(f"Expressão inválida: '{expression}'")

    result = additive_solve(expression)
    result = int(result) if int(result) == result else result

    return result

if __name__ == '__main__':
    while True:
        expression = input("> ")
        
        result = math_eval(expression)

        print(result)
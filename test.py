#!/bin/env python

from calculator import math_eval 

def test_math_eval():
    # Teste de números inteiros
    assert math_eval("2 + 3") == 5
    assert math_eval("10 - 4") == 6
    assert math_eval("6 * 7") == 42
    assert math_eval("8 / 2") == 4

    # Teste de números flutuantes
    assert math_eval("2.5 + 3.5") == 6.0
    assert math_eval("10.0 - 4.5") == 5.5
    assert math_eval("6.1 * 7.2") == 43.92
    assert math_eval("8.4 / 2.1") == 4.0

    # Teste de expressões mistas
    assert math_eval("2 + 3 * 4") == 14
    assert math_eval("10 - 4 / 2") == 8
    assert math_eval("6 * 7 + 2") == 44
    assert math_eval("8 / 2 - 1") == 3

    # Teste de espaços em branco
    assert math_eval(" 2 + 3 ") == 5
    assert math_eval(" 10 - 4 ") == 6
    assert math_eval(" 6 * 7 ") == 42
    assert math_eval(" 8 / 2 ") == 4

    print("Todos os testes passaram!")

# Executar os testes
test_math_eval()
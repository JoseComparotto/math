# Calculadora

Interpretador de expressões matemáticas para aplicar as teorias de Linguagens Formais e Automatos


## Gramática

```ebnf
<input> ::= <additive-expression>

<additive-expression> ::=
    <additive-expression>,
    <additive-operator>,
    <multiplicative-expression>
    | <multiplicative-expression>;

<multiplicative-expression> ::=
    <multiplicative-expression>,
    <multiplicative-operator>,
    <exponential-expression>
    | <exponential-expression>;

<exponential-expression> ::=
    <exponential-expression>,
    <exponential-operator>,
    <number>
    | <number>;

<number> ::= <integer-number> | <floating-number>;

<integer-number> ::= *<digit>;
<floating-number> ::= *<digit>, <decimal-separator>, *<digit>;

<digit> ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9';
<decimal-separator> ::= '.';
<additive-operator> ::= '+' | '-';
<multiplicative-operator> ::= '*' | '/';
<exponential-operator> ::= '^';

(* Notação EBNF - ISO/IEC 14977:1996 <https://www.iso.org/standard/26153.html> *)
```
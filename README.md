# Calculadora  

Interpretador de expressões matemáticas desenvolvido para aplicar conceitos de **Linguagens Formais e Autômatos**.  

Este projeto implementa um **parser recursivo descendente** para avaliar expressões matemáticas seguindo regras de precedência de operadores.  

## 📌 Funcionalidades  

- Suporte a números inteiros e de ponto flutuante.  
- Operações suportadas:  
  - **Adição (+)**  
  - **Subtração (-)**  
  - **Multiplicação (*)**  
  - **Divisão (/)**  
  - **Exponenciação (^)**  
- Suporte a espaços em branco dentro das expressões.  
- Implementação baseada em **expressões regulares** e **parsing recursivo**.  

## 📖 Gramática  

A seguinte gramática em **EBNF (Extended Backus-Naur Form)** descreve a estrutura das expressões suportadas:

```ebnf
input = additive-expression;

additive-expression =
    additive-expression,
    additive-operator,
    multiplicative-expression
    | multiplicative-expression;

multiplicative-expression =
    multiplicative-expression,
    multiplicative-operator,
    exponential-expression
    | exponential-expression;

exponential-expression =
    exponential-expression,
    exponential-operator,
    number
    | number;

number = integer-number | floating-number;

integer-number = digits;
floating-number = digits, decimal-separator, digits;

digits = digit, { digit };
digit = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9';
decimal-separator = '.';
additive-operator = '+' | '-';
multiplicative-operator = '*' | '/';
exponential-operator = '^';

(* Notação EBNF - ISO/IEC 14977:1996 <https://www.iso.org/standard/26153.html> *)
```

## 🚀 Como Usar

### 🔧 Requisitos

- Python 3.x

### ▶️ Executando a Calculadora

Para iniciar o interpretador interativo, execute o seguinte comando no terminal:

```sh
python calculadora.py
```

Isso iniciará um prompt onde você pode inserir expressões matemáticas para avaliação:

```plain
> 2 + 3 * 4
14
> 10 - 4 / 2
8
> 2 ^ 3 + 1
9
```


## 🧪 Testes

Para executar os testes automatizados, rode:

```sh
python test.py
```

Se todos os testes passarem, será exibida a mensagem:

```plain
Todos os testes passaram!
```

## 🏗️ Estrutura do Código

`calculadora.py`: Implementa o parser e a avaliação das expressões matemáticas.

`test.py`: Contém testes automatizados para validar o funcionamento da calculadora.


## 📜 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

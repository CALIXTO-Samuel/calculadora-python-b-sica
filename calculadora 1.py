#autor: Samuel
#data: 20/01/2026
import math

sinal = input('bem vindo a calculadora. escolha um sinal: +, -, /, *, **(elevado), RQ(raiz quadrada) ou o PI(valor de PI(20 casas depois da virgula)): ')

if sinal == '*':
    num1M = float(input('escreva o primeiro número: '))
    num2M = float(input('escreva o segundo número: '))
    multiplicacao = num1M * num2M
    print('O resultado dessa multiplicacão é:', multiplicacao)
    
if sinal == '+':
    num1A = float(input('escreva o primeiro número: '))
    num2A = float(input('escreva o segundo número: '))
    adicao = num1A + num2A
    print('O resultado dessa adição é:', adicao)
    
if sinal == '-':
    num1S = float(input('escreva o primeiro número a ser subtraído: '))
    num2S= float(input('escreva o segundo número: '))
    subtracao = num1S - num2S
    print('O resultado dessa subtração é:', subtracao)
    
if sinal == '/':
    num1D = float(input('escreva o primeiro número a ser dividido: '))
    num2D= float(input('escreva o segundo número: '))
    divisao = num1D / num2D
    resto = num1D % num2D
    round(resto, 2)
    print('O resultado dessa divisão é:', divisao, 'resto:', resto)
    
if sinal == '**':
    num1E = float(input('escreva o número a ser elevado: '))
    EXPo = float(input('escreva o expoente : '))
    elevado = num1E ** EXPo
    print(num1E, 'elevado a', EXPo, 'é:', elevado)
    
if sinal == 'RQ':
    num = float(input('escreva o número que será encontrada sua raiz quadrada: '))
    Raiz = math.sqrt(num)
    print(' a Raiz de', num, 'é:', Raiz)
    
if sinal == 'PI':
    valor_pi = math.pi
    round(valor_pi, 20)
    print(valor_pi)
    

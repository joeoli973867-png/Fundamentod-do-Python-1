# Exercício 2: Classificação de Triângulos
# Escreva um programa em Python que receba três comprimentos de
# lados de um triângulo e determine se o triângulo é equilátero,
# isósceles ou escaleno.
comprimento1 = int(input('Digite um Numero de Comprimento 1: '))
comprimento2 = int(input('Digite um Numero de Comprimento 2: '))
comprimento3 = int(input('Digite um Numero de Comprimento 3: '))
if comprimento1 == comprimento2 and comprimento1 == comprimento3:
    print('Triângulo Equilátero')
elif comprimento1 == comprimento2 or comprimento1 == comprimento3 or comprimento2 == comprimento3:
    print('Triângulo Isósceles')
else:
    print('Triângulo Escaleno')
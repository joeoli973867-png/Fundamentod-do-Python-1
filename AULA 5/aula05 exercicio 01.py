# Exercício 1: Verificação de Número Positivo
# Escreva um programa em Python que solicite ao usuário um número inteiro e verifique
# se o número é positivo, negativo ou zero.
# Em seguida, exiba uma mensagem apropriada de acordo
# com o resultado da verificação.
numero = int(input('Digite um Numero Inteiro: '))
if numero > 0:
    print('Numero Positivo')
elif numero == 0:
        print('Numero Zero')
else:
        print('Numero Negativo')